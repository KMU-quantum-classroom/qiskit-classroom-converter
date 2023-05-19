# pylint: disable=duplicate-code
"""
convert class
"""
import unittest

from qiskit import QuantumCircuit

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
        main.convert(input_value=input_value)
        # NotImplemented
        self.assertEqual(main.result, "|1>")

    def test_bra_ket_to_quantum_circuit(self):
        """Tests run method implementation."""
        main = BraketNotationToQuantumCircuitConverter()
        input_value = "|1>"
        main.convert(input_value=input_value)
        # NotImplemented
        self.assertEqual(main.result, "|1>")

    def test_matrix_to_quantum_circuit(self):
        """Tests run method implementation."""
        main = MatrixToQuantumCircuitConverter()
        input_value = [
            [1, 0, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0],
            [0, 1, 0, 0]
        ]
        main.convert(input_value=input_value)
        # NotImplemented
        self.assertEqual(main.result, [
            [1, 0, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0],
            [0, 1, 0, 0]
        ])

    def test_quantum_circuit_to_bra_ket(self):
        """Tests run method implementation."""
        main = QuantumCircuitToBraketNotationConverter()
        quantum_circuit = QuantumCircuit(1, 1)
        quantum_circuit.h(0)
        quantum_circuit.measure([0], [0])
        main.convert(input_value=quantum_circuit)
        # NotImplemented
        self.assertEqual(main.result, quantum_circuit)

    def test_quantum_circuit_to_matrix(self):
        """Tests run method implementation."""
        main = QuantumCircuitToMatrixConverter()
        quantum_circuit = QuantumCircuit(1, 1)
        quantum_circuit.h(0)
        quantum_circuit.measure([0], [0])
        main.convert(input_value=quantum_circuit)
        # NotImplemented
        self.assertEqual(main.result, quantum_circuit)
