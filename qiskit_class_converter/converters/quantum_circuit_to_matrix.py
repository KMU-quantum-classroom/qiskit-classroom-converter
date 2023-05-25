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
        matrix_list = {"gate": []}
        dag = self.qiskit.converters.circuit_to_dag(self.input_value)
        for layer in dag.layers():
            circuit = self.qiskit.converters.dag_to_circuit(layer['graph'])
            matrix_list["gate"].append(self.qiskit.quantum_info.Operator(circuit).to_matrix())
        matrix_list["result"] = self.qiskit.quantum_info.Operator(self.input_value).to_matrix()
        return matrix_list
