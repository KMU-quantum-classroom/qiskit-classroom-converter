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
        gate = self.qiskit.extensions.UnitaryGate(self.input_value)
        if self.option.get("label", False):
            gate.label = self.option.get("label", "")
        else:
            gate.label = str(self.input_value)
        return gate
