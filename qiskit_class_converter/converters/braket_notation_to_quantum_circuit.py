"""
Bra-ket Notation to QuantumCircuit Converter
"""
from qiskit_class_converter.converters.base import BaseConverter


class BraketNotationToQuantumCircuitConverter(BaseConverter):
    """
    Converter class
    """
    
    def actual_convert_action(self):
        self.logger.debug("bra-ket notation to quantum circuit")
        return self.input_value
