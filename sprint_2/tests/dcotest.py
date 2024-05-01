import unittest
import sys
sys.path.append("../src")
from dbo import dbo
from dbc import dbc

class TestDbo(unittest.TestCase):
    def setUp(self):
        # Mock a dbc instance for testing purposes
        con = DatabaseConnection()
    
        # Initialize a DBO instance with the mocked dbc
        testDataCube = Datacube(con, coverage_id='AvgTemperatureColorScaled', encode='image/png')


if __name__ == '__main__':
    unittest.main()
