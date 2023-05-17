"""
QuantumCircuit to Matrix Converter
"""
from src.interfaces.base import BaseConverter


class QuantumCircuitToMatrixConverter(BaseConverter):
    """
    Converter class
    """
    def actual_convert_action(self):
        print("quantum circuit -> matrix")
