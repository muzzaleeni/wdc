import sys
import unittest
from src.dbc import DatabaseConnection

class TestDatabaseConnection(unittest.TestCase):
    """
    Test case class for the DatabaseConnection object.

    This class contains test cases to verify the behavior of the DatabaseConnection object.
    """

    def test_initialization(self):
        """
        Test case to verify the initialization of the DatabaseConnection object.

        This test case checks if the DatabaseConnection object is properly initialized
        with the provided database URL. It ensures that the WCPS endpoint and the base WCS
        URL are correctly set.
        """
        # Set up a real DatabaseConnection instance
        db_url = "https://ows.rasdaman.org/rasdaman/ows"
        db_connection = DatabaseConnection(database_url=db_url)

        # Check if DatabaseConnection is properly initialized
        self.assertEqual(db_connection.WCPS_EndPoint, db_url)
        self.assertEqual(db_connection.base_wcs_url, db_url + "?service=WCS&version=2.1.0")

    def test_invalid_url_initialization(self):
        """
        Test case to verify the behavior when an invalid URL is provided during initialization.

        This test case checks the behavior of the DatabaseConnection object when an invalid
        database URL is provided during initialization. It verifies that the initialization
        raises a ValueError as expected.
        """
        with self.assertRaises(ValueError):
            # Attempt to create a DatabaseConnection instance with an invalid URL
            DatabaseConnection(database_url="invalid_url")

    def test_no_url_initialization(self):
        """
        Test case to verify the behavior when no URL is provided during initialization.

        This test case checks the behavior of the DatabaseConnection object when no database
        URL is provided during initialization. It ensures that the initialization raises a
        TypeError as expected.
        """
        with self.assertRaises(TypeError):
            # Attempt to create a DatabaseConnection instance without providing a URL
            DatabaseConnection()

if __name__ == '__main__':
    unittest.main()
