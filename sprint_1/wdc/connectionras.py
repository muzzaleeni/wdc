from .dbcf import DatabaseConnection
from .dcof import Datacube
from IPython.display import Image
from typing import Tuple, Optional
import requests

_service_endpoint = "https://ows.rasdaman.org/rasdaman/ows"
_base_wcs_url = _service_endpoint + "?service=WCS&version=2.0.1"
_base_wcps_url = _service_endpoint + "?service=WCS&version=2.0.1&request=ProcessCoverages"

class CoverageQuery:
    def __init__(self, base_wcs_url: str, base_wcps_url: str, coverage_id: str):
        self.base_wcs_url = base_wcs_url
        self.base_wcps_url = base_wcps_url
        self.coverage_id = coverage_id
        self.time_subset = None
        self.spatial_subset_e = None
        self.spatial_subset_n = None
        self.format = "image/jpeg"  

class Rasdaman:

    def __init__(self, service_endpoint: str = _service_endpoint, base_wcs_url: str = _base_wcs_url, base_wcps_url: str = _base_wcps_url):
        self.service_endpoint = service_endpoint
        self.base_wcs_url = base_wcs_url
        self.base_wcps_url = base_wcps_url

if __name__ == "__init__":

    rasdaman = Rasdaman()
    coverage_id = "S2_L2A_32631_TCI_60m"
    datacube = (rasdaman.get_coverage(coverage_id)
         .from_time("2021-04-09")
         .on((669960, 729960), (4990200, 5015220))
         )

    image = datacube.fetch()
    assert image is not None
