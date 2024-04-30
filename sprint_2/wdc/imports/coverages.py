from wdc.dbc import DatabaseConnection
from typing import Optional
from wdc import dbc
import requests
import xml.etree.ElementTree as ET
import urllib.parse

class Coverages:
    """
    Handles fetching a coverage from the server.
    """

    def __init__(self, connection: object, coverage_id: str, subset: Optional[str] = None, output_format: str = None):
        """
        Fetches the coverage for a given coverage ID.
        Args:
            connection (object): The connection object to the database.
            coverage_id (str): The ID of the coverage to be retrieved.
            subset (str): The subset of the coverage to retrieve.
            output_format (str): The format of the output data.
        """
        assert isinstance(connection, DatabaseConnection)
        self.connection = connection
        self.coverage_id = coverage_id
        self.subset = subset
        self.output_format = output_format
        if self.output_format is None:
            raise ValueError("Output format is required")
        else:
            assert self.output_format in Capacities(self.connection).get_encodings()
        self.base_wcs_url = connection.base_wcs_url
        self.request_url = self._construct_request_url()


    def _construct_request_url(self) -> str:

        request_url = f"{self.base_wcs_url}&request=GetCoverage&coverageId={self.coverage_id}&FORMAT={self.output_format}"
        if self.subset is not None:
            request_url += f"&SUBSET=ansi(\"{self.subset}\")"
        return request_url

    def fetch_coverage(self, query: Optional[str] = None) -> bytes:
        if query is not None:
            self.request_url += f"&query={query}"

        response = requests.get(self.request_url)
        response.raise_for_status()
        return response.content

class DescribeCoverage:
    """
      Class for handling DescribeCoverage requests.
    """

    def __init__(self, connection: object, coverage_id: str):
        """
        Initialize DescribeCoverage object with connection details and coverage ID.
        """
        assert isinstance(connection, dbc.DatabaseConnection)
        self._base_wcs_url = connection.base_wcs_url
        self._request = '&request=DescribeCoverage'
        self._coverage_id = coverage_id

    def describe_coverage_xml(self, cis: Optional[str] = None) -> str:
        """
        Fetches the description of the coverage from the server.
        Args:
          cis (str): Version of CIS.
        Returns:
          str: The XML description of the coverage.
        """
        # Check if the coverage ID and base WCS URL are set
        assert self._coverage_id is not None, "Coverage ID is required"
        assert self._base_wcs_url is not None, "Base WCS URL is required"

        if cis is not None:
            if cis not in ['1.0', '1.1']:
                raise ValueError(f"Unsupported CIS version: {cis}")
            else:
            # Send the request to the server including CIS version
                response = requests.get(f"{self._base_wcs_url}{self._request}&coverageId={self._coverage_id}&outputType=GeneralGridCoverage")
        else:
        # Send the request to the server without CIS versuon
            response = requests.get(f"{self._base_wcs_url}{self._request}&coverageId={self._coverage_id}")
        return response.text

    def describe(self, cis: Optional[str] = None) -> dict:
        """
        Parses the XML description of the coverage and returns a dictionary with the coverage information.
        Args:
          cis (str): Cis version
        Returns:
          A dictionary containing the parsed XML elements.
        """
        # First we define the namespaces as they make the code more readable
        ns = {
            'gml': 'http://www.opengis.net/gml/3.2',
            'gmlrgrid': 'http://www.opengis.net/gml/3.3/rgrid'
        }
        # Parse the XML response from the server
        root = ET.fromstring(self.describe_coverage_xml(cis))

        # Find the envelope element which contains all the other elements
        envelope = root.find(".//gml:Envelope", namespaces=ns)
        axis_labels = envelope.get("axisLabels").split()
        uom_labels = envelope.get("uomLabels").split()

        # Extract the lower and upper corners of the envelope
        lower_corner = [x for x in envelope.find("./gml:lowerCorner", namespaces=ns).text.split()]
        upper_corner = [x for x in envelope.find("./gml:upperCorner", namespaces=ns).text.split()]

        # Extract the grid limits if they are present
        limits = root.find(".//gml:limits", namespaces=ns)

        low_values = None
        high_values = None
        # Now we handle the case of different XML formats that the server might return 
        # We handle only two cases here because those are the ones that we found (more can be added)
        if limits is not None:
            grid_envelope = limits.find("./gml:GridEnvelope", namespaces=ns)
            if grid_envelope is not None:
                # Extract the low and high values of the coverage
                low_element = grid_envelope.find("./gml:low", namespaces=ns)
                high_element = grid_envelope.find("./gml:high", namespaces=ns)
                if low_element is not None:
                    # Split the values and convert them to floats
                    low_values = [float(x) for x in low_element.text.split()]
                if high_element is not None:
                    high_values = [float(x) for x in high_element.text.split()]
            # If the limits element is not present, we try to find the domainSet element instead
        else:
            domain_set = root.find(".//gml:domainSet", namespaces=ns)
            if domain_set is not None:
                grid = domain_set.find(".//gmlrgrid:ReferenceableGridByVectors", namespaces=ns)
                if grid is not None:
                    grid_envelope = grid.find("./gml:limits/gml:GridEnvelope", namespaces=ns)
                    if grid_envelope is not None:
                        # Same as before, but inside of another element
                        low_element = grid_envelope.find("./gml:low", namespaces=ns)
                        high_element = grid_envelope.find("./gml:high", namespaces=ns)
                        if low_element is not None:
                            low_values = [float(x) for x in low_element.text.split()]
                        if high_element is not None:
                            high_values = [float(x) for x in high_element.text.split()]

        # Finally we create our dictionary
        info_dict = {}
        # We iterate over the axis labels and create a dictionary entry for each axis
        for i, (axis_label, uom_label) in enumerate(zip(axis_labels, uom_labels)):
            geo_extent = [lower_corner[i], upper_corner[i]]
            grid_extent = [low_values[i] if low_values is not None else None, high_values[i] if high_values is not None else None]
            info_dict[axis_label] = {"UoM": uom_label, "Geo Extent": geo_extent, "Grid Extent": grid_extent}

        return info_dict


class ProcessCoverage:
    """
    Handles processing a coverage on the server. Similar structure as GetCoverage.
    """
    # We receive the connection object and the query to be processed.
    def __init__(self, connection: object, query: str) -> None:
        assert isinstance(connection, DatabaseConnection)
        self.base_wcs_url = connection.base_wcs_url
        self.query = query
        self.request_url = self._construct_request_url()

    def _construct_request_url(self) -> str:
        request_url = f"{self.base_wcs_url}&request=ProcessCoverage"
        return request_url

    def fetch_coverage(self) -> bytes:
        self.request_url += f"&query={self.query_to_url()}"
        response = requests.get(self.request_url)
        response.raise_for_status()
        return response.content

    def query_to_url(self) -> str:
        """Converts the WCS Query Object to a URL-encoded string."""
        return urllib.parse.quote(self.query)

class Capacities:
    """
      Class for handling GetCapabilities requests.
    """

    def __init__(self, connection: object):
        """
        Initialize GetCapabilities object with connection details.
        Args:
          connection (database_connection.DatabaseConnection): The connection object to the database.
        """

        assert isinstance(connection, dbc.DatabaseConnection)
        self._base_wcs_url = connection.base_wcs_url
        self._request = '&request=GetCapabilities'

    def get_capabilities(self) -> str:
        """
        Send a GetCapabilities request to the server and return the response.
        """
        response = requests.get(f"{self._base_wcs_url}{self._request}")
        response.raise_for_status()
        return response.text

    def get_coverage_ids(self) -> list[str]:
        """
        Returns a list of coverage IDs from the GetCapabilities response.
        These can be useful later for knowing which datacubes are available.
        """
        root = ET.fromstring(self.get_capabilities())
        coverage_ids = [coverage_summary.find('wcs20:CoverageId', namespaces={'wcs20': 'http://www.opengis.net/wcs/2.0'}).text
            for coverage_summary in root.findall('wcs20:Contents/wcs20:CoverageSummary', namespaces={'wcs20': 'http://www.opengis.net/wcs/2.0'})]
        return coverage_ids

    def get_encodings(self) -> list[str]:
        """
        Returns a list of encodings from the GetCapabilities response.
        These can be useful later for knowing which encodings are available.
        """
        root = ET.fromstring(self.get_capabilities())

        encodings = root.findall('.//wcs20:formatSupported', namespaces={'wcs20': 'http://www.opengis.net/wcs/2.0'})

        supported_encodings = [encoding_elem.text for encoding_elem in encodings]
        return supported_encodings

