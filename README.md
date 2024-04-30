## !! Must read !!

## From sprint_1 to sprint_2

    The first sprint was hadcoding one query, the one in example on Teams channel, so the only functions we could make use of were the DataBaseConnection and some code from the Datacube object
    The parameters of the __init__ function of the CoverageQuery class from the sprint_1/wdc/connectionras.py have been integrated in sprint_2/wdc/wrapper/coverages.py classes and functions

- connectionras.py/ class CoverageQuery:

  - self.base_wcs_url = base_wcs_url
  - self.base_wcps_url = base_wcps_url
  - self.coverage_id = coverage_id
  - self.time_subset = None
  - self.spatial_subset_e = None
  - self.spatial_subset_n = None
  - self.format = "image/jpeg"

- wrapper/Coverages:
  - request_url = f"{self.base_wcs_url}&request=GetCoverage&coverageId={self.coverage_id}&FORMAT={self.output_format}
  - self.connection = connection
  - self.coverage_id = coverage_id
  - self.subset = subset
  - self.output_format = output_format

## Added files and directories

- 1- /jupyter_notebook/WDC.ipynb
- 2- /src/ operation.py
- 3- /test/
- 4- /wrapper/ coverages.py
- 5- wdc_playground.py

## Removed files and directories

- 1- /**pyscache**/
- 2- setingup.py
- 3- connectionras.py

## Sprint 2

# WDC Wrapper

This is a WCP package which generates WCPS queries and sends them to the rasdaman server for execution.
The response is processed and saved in corresponding format.

## Built with:

- Python

## File Structure

\--Sprint2_Pair4\
|--------\--sprint_2\
| |----\--jupyter_notebook\
| | --WDC.ipynb
| |----\--wdc\
| | |---dco.py
| | |---dbc.oy
| | |----\src\
| | |----\test\
| | |----\wrapper\
| | |---.DS_Store
| | |---coverages.py
| |--- requirements.txt
| |--- wdc_playground.py
|-------- README.md

## Getting Started

Before you start running the code you would need to import some libraries in python. Install requirements.txt before you run the project.

## Installation Guide

    # Clone the repository.
    https://github.com/Constructor-Uni-SE-non-official/Sprint2_Pair4

    # cd to sprint_2

    # Follow the usage example to be able to use the functionalities of the package [jupyter_notebook](https://github.com/Constructor-Uni-SE-non-official/Sprint2_Pair4/blob/main/sprint_2/jupyter_notebook/WDC.ipynb)

# Methods', clases' functionality specification

-
-
-

twice ##, three times "normal"

# Jubgiu

## jhvj
