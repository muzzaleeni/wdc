# Methods' and Classes' Functionality Specification

## DatabaseConnection Object

- `__init__(self, endpoint: str, service: str, version: str)`
  - **Initialization:** Handles the connection to the database using the provided endpoint URL, service, and version.

## DatacubeObject

### Datacube Class

- `__init__(self, connection: DatabaseConnection, coverage_id: str, encode: str)`
  - **Initialization:** Initializes a Datacube object with the specified database connection, coverage ID, and encoding parameter.

- `data(self, cis: str = None)`
  - **Data Retrieval:** Retrieves the description of the datacube from the server using the Coverage_id class.

- `fetch(self, subset: str = None)`
  - **Data Retrieval from Server:** Fetches the datacube from the server using the Coverages class.

- `slice(self, slices: dict = None) -> str:`
  - **Slice Operation:** Applies a subset operation to the datacube based on the given slices.

- `_apply_operation(self, operation: Action) -> None:`
  - **Applying Operations:** Applies the specified operation to the WCPS (Web Coverage Processing Service) query.

- `_generate_wcps_query(self) -> str:`
  - **WCPS Query Generation:** Generates the WCPS query based on the list of operations applied to the datacube.

- `execute(self):`
  - **Executing Query:** Generates the WCPS query and executes it using the ProcessCoverage class, fetching the processed coverage from the server.

### Coverages.py

#### Coverages Class

- `__init__(self, connection: DatabaseConnection, coverage_id: str, subset: Optional[str] = None, output_format: str = 'image/tiff')`
  - **Initialization:** Initializes the Coverages object with the provided parameters.
  - Ensures that the connection object is of the correct type (DatabaseConnection).
  - Sets attributes for connection, coverage_id, subset, and output_format.
  - Checks if the output_format is provided and supported by the server by verifying it against the available encodings obtained from the Capacities class.

- `construct_request_url(self) -> str:`
  - **Construct Request URL:** Constructs the request URL based on the provided parameters.
  - Includes necessary parameters such as coverageId and FORMAT in the URL.
  - If a subset is provided, adds it to the URL with proper formatting.

- `fetch_coverage(self, query: Optional[str] = None) -> bytes:`
  - **Fetch Coverage:** Fetches the coverage from the server based on the constructed URL.
  - If a query is provided, appends it to the request URL.
  - Sends a GET request to the constructed URL using the requests.get method.
  - Checks for any errors in the response (response.raise_for_status()).
  - Returns the content of the response (response.content), which is the fetched coverage in bytes.

#### Coverage_id Class

- `__init__(self, connection: DatabaseConnection, coverage_id: str)`
  - **Initialization:** Initializes the Coverage_id object with a connection object and a coverage_id.
  - Sets the base WCS URL and request parameters needed for describing the coverage.

- `describe_coverage(self) -> str:`
  - **Describe Coverage:** Fetches the description of the coverage from the server and returns it as XML.
  - Constructs the request URL based on the provided parameters (coverage_id, base_wcs_url, outputType).
  - Sends a GET request to the server using the constructed URL.
  - Returns the text content of the response, which should be the XML description of the coverage.

- `parse_description(self, xml_description: str) -> dict:`
  - **Parse Description:** Parses the XML description of the coverage and returns a dictionary with the coverage information.
  - Defines namespaces for readability.
  - Parses the XML response obtained from the describe_coverage_xml method.
  - Returns the info_dict dictionary, which contains details about the coverage.

#### Capacities Class

- `__init__(self, connection: DatabaseConnection)`
  - **Initialization:** Initializes the Capacities object with a connection object representing the database connection.
  - Ensures that the provided connection object is of the correct type.
  - Sets the base WCS URL and request parameters needed for requests.

- `get_coverage_ids(self) -> List[str]:`
  - **Get Coverage IDs:** Retrieves coverage IDs from the server's capabilities.
  - Parses the XML response obtained from the get_capacities method.
  - Extracts coverage IDs from the XML by finding elements named 'wcs20:CoverageId' within 'wcs20:CoverageSummary' elements.
  - Returns a list of coverage IDs extracted from the capabilities.

#### Action Class

- `__init__(self, op_type: str, operands: List, **kwargs)`
  - **Initialization:** Encapsulates information about an action to be performed on a datacube.

