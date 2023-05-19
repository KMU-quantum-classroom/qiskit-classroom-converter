# pylint: disable=duplicate-code
"""
converter service class
"""
import unittest

from qiskit import QuantumCircuit

from qiskit_class_converter import ConversionService


class TestConverterServiceClass(unittest.TestCase):
    """Tests Service Impl class implementation."""

    def test_bra_ket_to_matrix_service(self):
        """Tests run Service method implementation."""
        input_value = "|1>"
        system = ConversionService(conversion_type="BRA_KET_TO_MATRIX")
        result = system.convert(input_value=input_value)
        # NotImplemented
        self.assertEqual(result, "|1>")

    def test_bra_ket_to_quantum_circuit_service(self):
        """Tests run Service method implementation."""
        input_value = "|1>"
        system = ConversionService(conversion_type="BRA_KET_TO_QC")
        result = system.convert(input_value=input_value)
        # NotImplemented
        self.assertEqual(result, "|1>")

    def test_matrix_to_quantum_circuit_service(self):
        """Tests run Service method implementation."""
        input_value = [
            [1, 0, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0],
            [0, 1, 0, 0]
        ]
        system = ConversionService(conversion_type="MATRIX_TO_QC")
        result = system.convert(input_value=input_value)
        # NotImplemented
        self.assertEqual(result, [
            [1, 0, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0],
            [0, 1, 0, 0]
        ])

    def test_quantum_circuit_to_bra_ket_service(self):
        """Tests run Service method implementation."""
        quantum_circuit = QuantumCircuit(1, 1)
        quantum_circuit.h(0)
        quantum_circuit.measure([0], [0])
        system = ConversionService(conversion_type="QC_TO_BRA_KET")
        result = system.convert(input_value=quantum_circuit)
        # NotImplemented
        self.assertEqual(result, quantum_circuit)

    def test_quantum_circuit_to_matrix_service(self):
        """Tests run Service method implementation."""
        quantum_circuit = QuantumCircuit(1, 1)
        quantum_circuit.h(0)
        quantum_circuit.measure([0], [0])
        system = ConversionService(conversion_type="QC_TO_MATRIX")
        result = system.convert(input_value=quantum_circuit)
        # NotImplemented
        self.assertEqual(result, quantum_circuit)
