# Tests

## Overview

`testdbc.py` checks the connection to the database, while `testdco.py` verifies the datacube operations. Both modules utilize the `unittest` framework for comprehensive testing.

### Database Connection Check

In `testdbc.py`, the test ensures that the database connection object's endpoint matches the actual endpoint of the database.

### Datacube Operations Check

In `testdco.py`, various aspects of the datacube class and its methods are tested. These include slicing the datacube, fetching data in different formats (image or CSV), modifying the datacube, and fetching images.

## Usage

To run the tests, execute the following commands from the root folder:

```bash
python3 -m unittest tests/testdbc.py
```
or

```bash
python3 -m unittest tests/testdco.py
```