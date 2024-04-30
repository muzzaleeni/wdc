from typing import List, Tuple


class Operation:
    """
    Class with an action to be executed in the datacube.
    """
    def __init__(self, op_type: str, operands: List, **kwargs):
        self.op_type = op_type
        self.operands = operands
        self.kwargs = kwargs


