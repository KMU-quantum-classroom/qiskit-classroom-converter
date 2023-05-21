"""
QuantumCircuit to Bra-ket Notation Converter
"""
from qiskit_class_converter.converters.base import BaseConverter


class QuantumCircuitToBraketNotationConverter(BaseConverter):
    """
    Converter class
    """
    def actual_convert_action(self):
        self.logger.debug("quantum circuit to bra-ket notation")
        return self.input_value
