"""
Bra-ket Notation to QuantumCircuit Converter
"""
from src.interfaces.base import BaseConverter


class BraketNotationToQuantumCircuitConverter(BaseConverter):
    """
    Converter class
    """
    def actual_convert_action(self):
        print("bra-ket notation -> quantum circuit")
