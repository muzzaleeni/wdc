class DatabaseConnection:
    """
    Represents a database connection to the WCPS server.
    
    Attributes:
    - WCPS_EndPoint (str): The URL of the WCPS server.
    - base_wcs_url (str): The base URL for making requests to the server.

    Example:
    ```
    connection = DatabaseConnection('http://example.com/wcps')
    ```
    """

    def __init__(self, database_url: str):
        """
        Initializes a DatabaseConnection object with the given WCPS server URL.
        
        Args:
        - database_url (str): The URL of the WCPS server.
        """
        self.WCPS_EndPoint = database_url 
        self.base_wcs_url = self.WCPS_EndPoint + "?service=WCS&version=2.1.0"
