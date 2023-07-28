#  Licensed to the Apache Software Foundation (ASF) under one
#  or more contributor license agreements.  See the NOTICE file
#  distributed with this work for additional information
#  regarding copyright ownership.  The ASF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.

# pylint: disable=duplicate-code
"""
converter service class
"""
import unittest

from qiskit import QuantumCircuit
from qiskit_class_converter import ConversionService, ConversionType
from qiskit_class_converter.converters.matrix_to_quantum_circuit \
    import MatrixToQuantumCircuitConverter


class TestConverterServiceClass(unittest.TestCase):
    """Tests Service Impl class implementation."""

    def test_bra_ket_to_matrix_service(self):
        """Tests run Service method implementation."""
        input_value = "|1>"
        system = ConversionService(conversion_type="BRA_KET_TO_MATRIX")
        result = system.convert(input_value=input_value)
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
        quantum_circuit = QuantumCircuit(2, 2)
        quantum_circuit.h(0)
        quantum_circuit.x(0)
        quantum_circuit.cx(0, 1)
        system = ConversionService(conversion_type="QC_TO_BRA_KET")
        result = system.convert(input_value=quantum_circuit)
        self.assertEqual(result, "(sqrt(2)/2)*|0> + (sqrt(2)/2)*|11>")

    def test_quantum_circuit_to_raw_bra_ket_service(self):
        """Tests run Service method implementation."""
        quantum_circuit = QuantumCircuit(2, 2)
        quantum_circuit.h(0)
        quantum_circuit.x(0)
        quantum_circuit.cx(0, 1)
        system = ConversionService(conversion_type="QC_TO_BRA_KET", option={"print": "raw"})
        result = system.convert(input_value=quantum_circuit)
        self.assertEqual(result, r"\frac{\sqrt{2}}{2} |00\rangle+\frac{\sqrt{2}}{2} |11\rangle")

    def test_quantum_circuit_to_simplify_bra_ket_service(self):
        """Tests run Service method implementation."""
        quantum_circuit = QuantumCircuit(2, 2)
        quantum_circuit.h(0)
        quantum_circuit.x(0)
        quantum_circuit.cx(0, 1)
        system = ConversionService(conversion_type="QC_TO_BRA_KET",
                                   option={"expression": "simplify"})
        result = system.convert(input_value=quantum_circuit)
        self.assertEqual(result, "sqrt(2)*(|0> + |11>)/2")

    def test_quantum_circuit_to_expand_bra_ket_service(self):
        """Tests run Service method implementation."""
        quantum_circuit = QuantumCircuit(2, 2)
        quantum_circuit.h(0)
        quantum_circuit.x(0)
        quantum_circuit.cx(0, 1)
        system = ConversionService(conversion_type="QC_TO_BRA_KET",
                                   option={"expression": "expand"})
        result = system.convert(input_value=quantum_circuit)
        self.assertEqual(result, "sqrt(2)*|0>/2 + sqrt(2)*|11>/2")

    def test_quantum_circuit_to_simplify_raw_bra_ket_service(self):
        """Tests run Service method implementation."""
        quantum_circuit = QuantumCircuit(2, 2)
        quantum_circuit.h(0)
        quantum_circuit.x(0)
        quantum_circuit.cx(0, 1)
        system = ConversionService(conversion_type="QC_TO_BRA_KET",
                                   option={"expression": "simplify", "print": "raw"})
        result = system.convert(input_value=quantum_circuit)
        self.assertEqual(result, r"\frac{\sqrt{2} \left({\left|0\right\rangle } + "
                                 r"{\left|11\right\rangle }\right)}{2}")

    def test_quantum_circuit_to_expand_raw_bra_ket_service(self):
        """Tests run Service method implementation."""
        quantum_circuit = QuantumCircuit(2, 2)
        quantum_circuit.h(0)
        quantum_circuit.x(0)
        quantum_circuit.cx(0, 1)
        system = ConversionService(conversion_type="QC_TO_BRA_KET",
                                   option={"expression": "expand", "print": "raw"})
        result = system.convert(input_value=quantum_circuit)
        self.assertEqual(result, r"\frac{\sqrt{2} {\left|0\right\rangle }}{2} + "
                                 r"\frac{\sqrt{2} {\left|11\right\rangle }}{2}")

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
