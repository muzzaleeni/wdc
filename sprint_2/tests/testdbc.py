import unittest
import sys
sys.path.append("..")
from wdc.dbc import DatabaseConnection

# Very simple test class for the Database Connection object
class TestDatabaseConnection(unittest.TestCase):
    def setUp(self):
        self.db_connection = DatabaseConnection()

    def test_initialization(self):
        self.assertEqual(self.db_connection.WCPS_EndPoint, "https://ows.rasdaman.org/rasdaman/ows")
        self.assertEqual(self.db_connection.serverOptions["service"], "WCS")
        self.assertEqual(self.db_connection.serverOptions["version"], "2.1.0")
        self.assertEqual(self.db_connection.base_wcs_url, "https://ows.rasdaman.org/rasdaman/ows?service=WCS&version=2.1.0")

if __name__ == '__main__':
    unittest.main()
