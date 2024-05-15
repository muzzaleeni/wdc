import sys
sys.path.append("./src")

import unittest
from unittest.mock import Mock
from src.dco import Datacube

class TestDatacube(unittest.TestCase):
    """
    Test case class for the Datacube object.

    This class contains test cases to verify the behavior of the Datacube object
    and its methods.
    """

    def setUp(self):
        """
        Set up method to create a mock DatabaseConnection object before each test case.
        """
        self.mock_connection = Mock()

    def test_slice_and_execute_image(self):
        """
        Test case to verify slicing and executing a Datacube with an image encoding.

        This test case ensures that slicing and executing a Datacube object with an
        image encoding results in the expected behavior, including calling the
        describe and fetch_coverage methods of the DatabaseConnection mock.
        """
        # Mock describe and fetch_coverage methods
        self.mock_connection.describe.return_value = {"axes": ["ansi", "Lat", "Lon"], "shape": [365, 180, 360]}
        self.mock_connection.fetch_coverage.return_value = b'PNG_IMAGE_DATA'

        # Create Datacube 
        datacube = Datacube(self.mock_connection, coverage_id='AvgTemperatureColorScaled', encode='image/png')

        # Slice datacube
        modify_ans = {"ansi": "2000-04"}
        slice_datacube = datacube.slice(modify_ans)

        # Mock fetch_coverage method after slice operation
        slice_datacube.execute()

        # Assert calls
        self.mock_connection.describe.assert_called_once_with('AvgTemperatureColorScaled')
        self.mock_connection.fetch_coverage.assert_called_once()

    def test_slice_and_execute_csv(self):
        """
        Test case to verify slicing and executing a Datacube with a CSV encoding.

        This test case ensures that slicing and executing a Datacube object with a
        CSV encoding results in the expected behavior, including calling the
        describe and fetch_coverage methods of the DatabaseConnection mock.
        """
        # Mock describe and fetch_coverage methods
        self.mock_connection.describe.return_value = {"axes": ["ansi", "Lat", "Lon"], "shape": [365, 180, 360]}
        self.mock_connection.fetch_coverage.return_value = b'CSV_DATA'

        # Create and slice Datacube
        datacube = Datacube(self.mock_connection, coverage_id='AvgLandTemp', encode='text/csv')
        subset = {"ansi": ("2014-01", "2014-12"), "Lat": (53.08), "Lon": (8.80)}
        slice_datacube = datacube.slice(subset)

        # Mock fetch_coverage method after slicing
        slice_datacube.execute()

        # Assert calls
        self.mock_connection.describe.assert_called_once_with('AvgLandTemp')
        self.mock_connection.fetch_coverage.assert_called_once()

    def test_get_image(self):
        """
        Test case to verify fetching an image Datacube.

        This test case ensures that fetching an image Datacube object results in
        the expected behavior, including calling the fetch_coverage method of the
        DatabaseConnection mock.
        """
        # Mock fetch_coverage method
        self.mock_connection.fetch_coverage.return_value = b'PNG_IMAGE_DATA'

        # Create Datacube 
        datacube = Datacube(self.mock_connection, coverage_id='AvgTemperatureColorScaled', encode='image/png')

        # Fetch datacube
        datacube.get('2014-07')

        # Assert call
        self.mock_connection.fetch_coverage.assert_called_once()

    def test_modify_and_execute_image(self):
        """
        Test case to verify modifying and executing an image Datacube.

        This test case ensures that modifying and executing an image Datacube object
        results in the expected behavior, including calling the describe and fetch_coverage
        methods of the DatabaseConnection mock.
        """
        # Mock describe and fetch_coverage methods
        self.mock_connection.describe.return_value = {"axes": ["ansi", "Lat", "Lon"], "shape": [365, 180, 360]}
        self.mock_connection.fetch_coverage.return_value = b'MODIFIED_PNG_IMAGE_DATA'

        # Create and modify Datacube 
        datacube = Datacube(self.mock_connection, coverage_id='AvgTemperatureColorScaled', encode='image/png')
        modify_ans1 = {"ansi": "2000-02-01"}
        subset_dc = datacube.slice(modify_ans1)

        # Mock fetch_coverage method after modification
        subset_dc.execute()

        # Assert calls
        self.mock_connection.describe.assert_called_once_with('AvgTemperatureColorScaled')
        self.mock_connection.fetch_coverage.assert_called_once()

if __name__ == '__main__':
    unittest.main()
