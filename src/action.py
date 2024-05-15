from typing import List, Tuple

class Action:
    """
    Represents an action to be executed on the datacube.

    Parameters:
    - op_type (str): Type of operation to be performed.
    - operands (List): List of operands for the operation.
    - **kwargs: Additional keyword arguments for the operation.

    Attributes:
    - op_type (str): Type of operation.
    - operands (List): Operands for the operation.
    - kwargs (dict): Additional keyword arguments.

    Example:
    ```
    action = Action('slice', ['Lat', 'Lon'], ansi='2000-04')
    ```
    """
    def __init__(self, op_type: str, operands: List, **kwargs):
        """
        Initialize the Action object with the specified operation type, operands, and optional keyword arguments.
        """
        self.op_type = op_type
        self.operands = operands
        self.kwargs = kwargs
