from .dbcf import DatabaseConnection

class Datacube:
    def __init__(self, dbc):
        self.dbcf = dbc

    def fetch_png_image(self, query, output_file='test.png'):
        """get an image using a WCPS query and save it to files  """
        self.dbcf.execute_query(query, output_file)
