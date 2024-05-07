## !! Must read !!

## From sprint_1 to sprint_2

    The first sprint was hardcoding one query, the one in example on Teams channel, so the only functions we could make use of were the DataBaseConnection and some code from the Datacube object
    The parameters of the __init__ function of the CoverageQuery class from the sprint_1/wdc/connectionras.py have been integrated in sprint_2/wdc/wrapper/coverages.py classes and functions

- sprint_1/connectionras.py/ class CoverageQuery:

  - self.base_wcs_url = base_wcs_url
  - self.base_wcps_url = base_wcps_url
  - self.coverage_id = coverage_id
  - self.time_subset = None
  - self.spatial_subset_e = None
  - self.spatial_subset_n = None
  - self.format = "image/jpeg"

- sprint_2/wdc/wrapper/Coverages:
  - request_url = f"{self.base_wcs_url}&request=GetCoverage&coverageId={self.coverage_id}&FORMAT={self.output_format}
  - self.connection = connection
  - self.coverage_id = coverage_id
  - self.subset = subset
  - self.output_format = output_format

## Added files and directories

- 1- /jupyter_notebook/WDC.ipynb
- 2- /src/ action.py
- 3- /tests/
- 4- /wrapper/ coverages.py
- 5- wdc_playground.py
- 6- /lazyuser/**init**.py, lazyuserdco.py, user_select.py, queries.py
- 7- requirements.txt
- 8- README.md

## Removed files and directories

- 1- /**pyscache**/
- 2- setingup.py
- 3- connectionras.py

---

# Sprint 2

# WDC Wrapper

This is a WCP package which generates WCPS queries and sends them to the rasdaman server for execution.
The response is processed and saved in corresponding format.

## Built with:

- Python

## File Structure

```
\--Sprint2_Pair4\
|--------\--sprint_2\
|         |----\--jupyter_notebook\
|         |           |---WDC.ipynb
|         |----\--wdc\
|         |           |---dco.py
|         |           |---dbc.oy
|         |           |----\src\
|         |           |         |---action.py
|         |           |----\test\
|         |           |         |---
|         |           |         |---
|         |           |----\wrapper\
|         |           |            |---.DS_Store
|         |           |            |---coverages.py
|         |           |-----\lazyuser\
|         |                          |---lazyuserdco.py
|         |                          |---queries.py
|         |                          |---run_queries.py
|         |                          |---user_select.py
|         |--- requirements.txt
|         |--- wdc_playground.py
|-------- README.md
```

## Getting Started

Before you start running the code you would need to import some libraries in python. Install requirements.txt before you run the project.

## Installation Guide

    # Clone the repository.
    https://github.com/Constructor-Uni-SE-non-official/Sprint2_Pair4

    # cd to sprint_2

Follow the usage example to be able to use the functionalities of the package [jupyter_notebook][1].

[1]: https://github.com/Constructor-Uni-SE-non-official/Sprint2_Pair4/blob/main/sprint_2/jupyter_notebook/WDC.ipynb "jupyter_notebook"

# Tests

All testing-related files are found in the \tests directory inside \wdc. There are two files, testdbc.py and testdco.py, which test the DatabaseConnection and DataCube classes respectively.

Running the tests is easy. In your terminal, after cloning the repository, simply cd to the sprint_2 folder, and run either of the two files, depending on which class you wish to test:

```
python3 wdc/tests/testdbc.py
python3 wdc/tests/testdco.py
```

There is a known bug in python where test files cannot read packages outside the test folder. If this happens to you, a simple fix is to change the

```
sys.path.append("..")
```

line (line 3 for testdbc and 4 for testdco) to import the absolute path of sprint_2/wdc.

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
```

## WDC Playground

- To see the exapmles explained in the jupyter notebook:
  - clone the repository, link in the Installation Guide
  - install requirements.txt
  - cd sprint_2
  - On Unix
    - python3 wdc_playground.py
  - In windows
    - python wdc_playground.py

# Lazy-user interaction

In order to send queries to the server without the effort of creating a DatabaseConnection, and adding the parameters of the Datacube manually,
you can see the result of many quries stored on lazyuser/queries.py by doing the following:

    1- Follow the Installation guide to clone and install requirements
    2- cd sprint_2/wdc
    3- python3 -m lazyuser.run_queries

The results are stored in lazyuser/outputs

## For making use of the Lazy-user feature, and also select the queries you want to get the results from:

    1- Follow the Installation guide to clone the repo and install the requirements.
    2- cd sprint_2/wdc
    3-python3 -m lazyuser.user_select

Follow the documentation to see the exact usage and results [jupyter_notebook][1].

[1]: https://github.com/Constructor-Uni-SE-non-official/Sprint2_Pair4/blob/main/sprint_2/jupyter_notebook/WDC.ipynb "jupyter_notebook"
