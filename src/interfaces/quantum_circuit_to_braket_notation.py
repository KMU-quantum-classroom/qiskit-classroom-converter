"""
QuantumCircuit to Bra-ket Notation Converter
"""
from src.interfaces.base import BaseConverter


class QuantumCircuitToBraketNotationConverter(BaseConverter):
    """
    Converter class
    """
    def actual_convert_action(self):
        print("quantum circuit -> bra-ket notation")
