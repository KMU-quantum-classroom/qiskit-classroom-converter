"""
Bra-ket Notation to Matrix Converter
"""
from qiskit_class_converter.converters.base import BaseConverter


class BraketNotationToMatrixConverter(BaseConverter):
    """
    Converter class
    """
    def actual_convert_action(self):
        self.logger.debug("bra-ket notation to matrix")
        return self.input_value
