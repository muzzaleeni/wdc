# Methods', clases' functionality specification

## DatabaseConnection object

```
- __init__(self)
  Handles the connection to the database using the endpoint url, service, and version.
```

## DatacubeObject

- Datacube class:

```
__init__:connection, coverage_id, encoding parameter
1- Initialization: The constructor initializes a Datacube object with the following parameters:

data(self, cis: str = None)
2- Data Retrieval: The data method retrieves the description of the datacube from the server using the Coverage_id class.

fetch(self, subset: str = None)
3- Data Retrieval from Server: The fetch method fetches the datacube from the server using the Coverages class.

slice(self, slices: dict = None) -> str:
4- slice operation: The slice method applies a subset operation to the datacube based on the given slices.

5- Applying Operations: The \_apply_operation method applies the specified operation to the WCPS (Web Coverage Processing Service) query.

generate_wcps_query(self) -> query:
6- WCPS Query Generation: The \_generate_wcps_query method generates the WCPS query based on the list of operations applied to the datacube.

execute(self):
7- Executing Query: The execute method generates the WCPS query and executes it using the ProcessCoverage class, fetching the processed coverage from the server.
```

```
coverages.py -> Handles retrieving of the reponses from the server and proccessing that response depending on its type.
## Coverages
 __init__
 Parameters:
     -connection: The connection object to the database.
     -coverage_id: The ID of the coverage to be fetched.
     -subset (optional): The subset of the coverage to retrieve.
     -output_format: The format of the output data.
    It ensures that the connection object is of the correct type (DatabaseConnection).
    Sets attributes for connection, coverage_id, subset, and output_format.
    Checks if the output_format is provided and supported by the server by verifying it against the available encodings obtained from the Capacities class.

construct_request_url(self) -> url:
Parameters:
    -coverage_id
    -subset
    -output_format
Constructs the request URL based on the provided parameters It includes the necessary parameters such as coverageId and FORMAT in the URL.
If a subset is provided, it adds it to the URL with proper formatting.

fetch_coverage(self, query: Optional[str] = None)
    -It takes an optional query parameter to include in the request URL.
    -If a query is provided, it appends it to the request URL.
    -It sends a GET request to the constructed URL using the requests.get method.
    -Checks for any errors in the response (response.raise_for_status()).
Returns the content of the response (response.content), which is the fetched coverage in bytes.

## Coverage_id:
__init__
    It initializes the object with a connection object and a coverage_id.
    It sets the base WCS URL and request parameters needed for describing the coverage.

describe_coverage_
    This method fetches the description of the coverage from the server and returns it as XML.
    It constructs the request URL based on the provided parameters (coverage_id, base_wcs_url, outputType).
    It sends a GET request to the server using the constructed URL.
    Returns the text content of the response, which should be the XML description of the coverage.

describe
    This method parses the XML description of the coverage and returns a dictionary with the coverage information.
    It defines namespaces for readability.
    It parses the XML response obtained from the describe_coverage_xml method.
    Returns the info_dict dictionary, which contains details about the coverage.

## Capacities
__init__
    It initializes the object with a connection object representing the database connection.
    It ensures that the provided connection object is of the correct type
    It sets the base WCS URL and request parameters needed for requests.

get_coverage
    Retrieves coverage IDs from the server's capabilities.
    Parses the XML response obtained from the get_capacities method
    Extracts coverage IDs from the XML by finding elements named 'wcs20:CoverageId' within 'wcs20:CoverageSummary' elements.
    Returns a list of coverage IDs extracted from the capabilities

## Action
__init__(self, op_type: str, operands: List, **kwargs)
    Encapsulate information about an action to be performed on a datacube.
