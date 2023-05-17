"""
Matrix to Quantum Circuit Converter
"""
from src.interfaces.base import BaseConverter


class MatrixToQuantumCircuitConverter(BaseConverter):
    """
    Converter class
    """
    def actual_convert_action(self):
        print("matrix -> quantum circuit")
