# pylint: disable=duplicate-code
"""
converter service class
"""
import unittest

from qiskit import QuantumCircuit
from qiskit_class_converter.converters.matrix_to_quantum_circuit \
    import MatrixToQuantumCircuitConverter

from qiskit_class_converter import ConversionService, ConversionType


class TestConverterServiceClass(unittest.TestCase):
    """Tests Service Impl class implementation."""

    def test_bra_ket_to_matrix_service(self):
        """Tests run Service method implementation."""
        input_value = "|1>"
        system = ConversionService(conversion_type="BRA_KET_TO_MATRIX")
        result = system.convert(input_value=input_value)
        # NotImplemented
        self.assertIsNotNone(result)

    def test_bra_ket_to_quantum_circuit_service(self):
        """Tests run Service method implementation."""
        input_value = "|1>"
        system = ConversionService(conversion_type="BRA_KET_TO_QC")
        result = system.convert(input_value=input_value)
        # NotImplemented
        self.assertIsNotNone(result)

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
        self.assertIsNotNone(result)

    def test_quantum_circuit_to_bra_ket_service(self):
        """Tests run Service method implementation."""
        quantum_circuit = QuantumCircuit(1, 1)
        quantum_circuit.h(0)
        quantum_circuit.measure([0], [0])
        system = ConversionService(conversion_type="QC_TO_BRA_KET")
        result = system.convert(input_value=quantum_circuit)
        # NotImplemented
        self.assertIsNotNone(result)

    def test_quantum_circuit_to_matrix_service(self):
        """Tests run Service method implementation."""
        quantum_circuit = QuantumCircuit(2)
        quantum_circuit.cx(0, 1)
        system = ConversionService(conversion_type="QC_TO_MATRIX")
        result = system.convert(input_value=quantum_circuit)
        self.assertIsNotNone(result)

    def test_conversion_type(self):
        """Tests run Service Type implementation."""
        self.assertEqual(ConversionType.MATRIX_TO_QC.value, MatrixToQuantumCircuitConverter)
