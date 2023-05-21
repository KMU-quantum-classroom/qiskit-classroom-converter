"""
Matrix to Quantum Circuit Converter
"""
from qiskit_class_converter.converters.base import BaseConverter


class MatrixToQuantumCircuitConverter(BaseConverter):
    """
    Converter class
    """
    def actual_convert_action(self):
        self.logger.debug("matrix to quantum circuit")
        return self.qiskit.extensions.UnitaryGate(self.input_value)
