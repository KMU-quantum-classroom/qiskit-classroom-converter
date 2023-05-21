"""
QuantumCircuit to Matrix Converter
"""
from qiskit_class_converter.converters.base import BaseConverter


class QuantumCircuitToMatrixConverter(BaseConverter):
    """
    Converter class
    """
    def actual_convert_action(self):
        self.logger.debug("quantum circuit to matrix")
        self.input_value = self.qiskit.quantum_info.Operator(self.input_value)
        return self.input_value.to_matrix()
