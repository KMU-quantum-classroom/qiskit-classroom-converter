# pylint: disable=duplicate-code
"""
convert class
"""
import unittest
import warnings

from numpy import array
from qiskit import QuantumCircuit
from qiskit.circuit import Instruction

from qiskit_class_converter.converters.braket_notation_to_matrix \
    import BraketNotationToMatrixConverter
from qiskit_class_converter.converters.braket_notation_to_quantum_circuit \
    import BraketNotationToQuantumCircuitConverter
from qiskit_class_converter.converters.matrix_to_quantum_circuit \
    import MatrixToQuantumCircuitConverter
from qiskit_class_converter.converters.quantum_circuit_to_braket_notation \
    import QuantumCircuitToBraketNotationConverter
from qiskit_class_converter.converters.quantum_circuit_to_matrix \
    import QuantumCircuitToMatrixConverter


class TestConvertClass(unittest.TestCase):
    """Tests Impl class implementation."""

    def test_bra_ket_to_matrix(self):
        """Tests run method implementation."""
        main = BraketNotationToMatrixConverter()
        input_value = "|1>"
        result = main.convert(input_value=input_value)
        # NotImplemented
        self.assertEqual(result, "|1>")

    def test_bra_ket_to_quantum_circuit(self):
        """Tests run method implementation."""
        main = BraketNotationToQuantumCircuitConverter()
        input_value = "|1>"
        result = main.convert(input_value=input_value)
        # NotImplemented
        self.assertEqual(result, "|1>")

    def test_matrix_to_quantum_circuit(self):
        """Tests run method implementation."""
        main = MatrixToQuantumCircuitConverter()
        input_value = [
            [1, 0, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0],
            [0, 1, 0, 0]
        ]
        expect_value = Instruction(name='unitary', num_qubits=2, num_clbits=0,
                                   params=[array([[1. + 0.j, 0. + 0.j, 0. + 0.j, 0. + 0.j],
                                                  [0. + 0.j, 0. + 0.j, 0. + 0.j, 1. + 0.j],
                                                  [0. + 0.j, 0. + 0.j, 1. + 0.j, 0. + 0.j],
                                                  [0. + 0.j, 1. + 0.j, 0. + 0.j, 0. + 0.j]])])
        result = main.convert(input_value=input_value)
        self.assertEqual(str(result), str(expect_value))

    def test_quantum_circuit_to_bra_ket(self):
        """Tests run method implementation."""
        main = QuantumCircuitToBraketNotationConverter()
        quantum_circuit = QuantumCircuit(2, 2)
        quantum_circuit.h(0)
        quantum_circuit.x(0)
        quantum_circuit.cx(0, 1)
        result = main.convert(input_value=quantum_circuit)
        self.assertEqual(result, "(sqrt(2)/2)*|0> + (sqrt(2)/2)*|11>")

    def test_quantum_circuit_to_matrix(self):
        """Tests run method implementation."""
        warnings.filterwarnings('ignore')
        main = QuantumCircuitToMatrixConverter()
        quantum_circuit = QuantumCircuit(2, 2)
        quantum_circuit.cx(0, 1)
        result = main.convert(input_value=quantum_circuit)
        expect_value = array([
            [1, 0, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0],
            [0, 1, 0, 0]
        ])
        self.assertTrue((result["result"].astype(int) & expect_value).any())