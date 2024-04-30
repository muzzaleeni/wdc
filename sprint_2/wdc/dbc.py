
class DatabaseConnection:
    """A class representing a database connection to the WCPS server"""

    def __init__(self):
        self.WCPS_EndPoint = "https://ows.rasdaman.org/rasdaman/ows"
        self.serverOptions = {
            "service": "WCS",
            "version": "2.1.0",
        }
        self.base_wcs_url = self.WCPS_EndPoint + "?service=WCS&version=2.1.0"
