from dbc import DatabaseConnection
from coverages import ProcessCoverage, Coverage_id, Coverages, Capacities
from action import Action 
from typing import List, Tuple

class Datacube:
    """
    Represents a datacube and provides methods for interacting with it.
    """

    def __init__(self, connection: DatabaseConnection, coverage_id: str, encode: str = None):
        """
        Initializes a Datacube object.

        Args:
            connection (DatabaseConnection): The connection object to the database.
            coverage_id (str): The ID of the coverage associated with the datacube.
            encode (str, optional): The encoding format for the data. Defaults to None.
        
        Raises:
            ValueError: If an invalid encoding format is provided.
        """
        self.connection = connection
        self.coverage_id = coverage_id
        self._info = self.data()
        self.operations = []
        self.encode = encode
        self.covExpr = "$c"
        if self.encode and self.encode not in Capacities(self.connection).get_encodings():
            raise ValueError(f"Invalid encoding: {encode}")

    def _generate_wcps_query(self) -> str:
        """
        Generates a WCPS query based on the specified operations.

        Returns:
            str: The WCPS query.
        """
        query = f"for $c in ({self.coverage_id}) return "
        for op in self.operations:
            return_query = f"{self._apply_operation(op)}"
        return_query = self.encode_format(return_query)
        query += return_query
        return query

    def execute(self):
        """
        Executes the generated WCPS query and fetches the coverage data.

        Returns:
            bytes: The fetched coverage data.
        
        Raises:
            ValueError: If no operations are specified.
        """
        if not self.operations:
            raise ValueError("No operations specified")
        query = self._generate_wcps_query()

        get_request = ProcessCoverage(self.connection, query=query)
        self.covExpr = "$c"
        return get_request.fetch_coverage()
        
    def data(self, cis: str = None) -> dict:
        """
        Retrieves information about the datacube.

        Args:
            cis (str, optional): The CIS version. Defaults to None.

        Returns:
            dict: Information about the datacube.
        """
        describe_request = Coverage_id(self.connection, self.coverage_id)
        return describe_request.describe(cis)

    def get(self, subset: str = None) -> bytes:
        """
        Fetches datacube from the server.

        Args:
            subset (str, optional): The subset of the datacube to fetch. Defaults to None.

        Returns:
            bytes: The fetched datacube.
        """
        get_request = Coverages(self.connection, self.coverage_id, subset, self.encode)
        return get_request.fetch_coverage()

    def slice(self, slices: dict = None) -> str:
        """
        Slices the datacube based on the given data.

        Args:
            slices (dict, optional): A dictionary containing the slices for each axis. Defaults to None.

        Returns:
            str: The sliced datacube.
        
        Raises:
            ValueError: If an invalid axis name or selection type is provided.
        """
        op = Action('subset', [self], slices=slices)
        self.operations.append(op)
        return self


    def _apply_operation(self, op: Action) -> str:
        """
        Applies the given operation to the datacube.

        Args:
            op (Action): The operation to apply.

        Returns:
            str: The applied operation.
        """
        op_type = op.op_type
        if op_type == 'subset':
            slices = op.kwargs['slices']
            query = self._apply_slice(slices)
        elif op_type == 'scale':
            scale_factor = op.kwargs.get('scale_factor')
            scale_expr = self._apply_scale(scales=scale_factor)
            query = f"{scale_expr}"
        return query

    def _apply_slice(self, slices: dict = None) -> str:
        """
        Applies the slice operation to the datacube.

        Args:
            slices (dict, optional): A dictionary containing the slices for each axis. Defaults to None.

        Returns:
            str: The sliced datacube.

        Raises:
            ValueError: If an invalid axis name or selection type is provided.
        """
        axis_labels = self._info.keys()

        subset_expr = []
        for axis, selection in slices.items():
            if axis not in axis_labels:
                raise ValueError(f"Invalid axis name: {axis}, possible axes are: {axis_labels}")
            if isinstance(selection, (int, float)):
                                subset_expr.append(f"{axis}({selection})")
            elif isinstance(selection, str) or (isinstance(selection, tuple) and all(isinstance(s, str) for s in selection)):
                if isinstance(selection, tuple):
                    lo, hi = selection
                    selection = f'"{lo}":"{hi}"'
                elif isinstance(selection, str):
                    selection = f'"{selection}"'
                subset_expr.append(f'{axis}({selection})')
            elif isinstance(selection, tuple):
                lo, hi = selection
                subset_expr.append(f"{axis}({lo}:{hi})")
            else:
                raise ValueError(f"Invalid selection type for axis {axis}: {type(selection)}")
        subset_query = f"{self.covExpr}[{', '.join(subset_expr)}]"
        self.covExpr = subset_query

        return subset_query

    def encode_format(self, query: str) -> str:
        """
        Encodes the query with the specified encoding format.

        Args:
            query (str): The query to encode.

        Returns:
            str: The encoded query.
        """
        if self.encode is not None:
            return f"encode({query}, \"{self.encode}\")"
        return query

