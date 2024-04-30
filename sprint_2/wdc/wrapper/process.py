from typing import Optional
from wdc.database_connection import DatabaseConnection
import requests
import urllib.parse

class ProcessCoverage:
    """
    Handles processing a coverage on the server. Similar structure as GetCoverage.
    """
    # We receive the connection object and the query to be processed.
    def __init__(self, connection: object, query: str) -> None:
        assert isinstance(connection, DatabaseConnection)
        self.base_wcs_url = connection.base_wcs_url
        self.query = query
        self.request_url = self._construct_request_url()

    def _construct_request_url(self) -> str:
        request_url = f"{self.base_wcs_url}&request=ProcessCoverage"
        return request_url

    def fetch_coverage(self) -> bytes:
        self.request_url += f"&query={self.query_to_url()}"
        response = requests.get(self.request_url)
        response.raise_for_status()
        return response.content

    def query_to_url(self) -> str:
        """Converts the WCS Query Object to a URL-encoded string."""
        return urllib.parse.quote(self.query)
