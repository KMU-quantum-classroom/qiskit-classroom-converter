"""
Bra-ket Notation to Matrix Converter
"""
from src.interfaces.base import BaseConverter


class BraketNotationToMatrixConverter(BaseConverter):
    """
    Converter class
    """
    def actual_convert_action(self):
        print("bra-ket notation -> matrix")
