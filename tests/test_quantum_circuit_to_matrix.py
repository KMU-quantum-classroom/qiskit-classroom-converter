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

from numpy import array
from numpy.testing import assert_array_equal
from qiskit import QuantumCircuit

from qiskit_class_converter import ConversionService


class TestQcToMatrixClass(unittest.TestCase):
    """Tests Service Impl class implementation."""

    def test_qc_to_matrix_gate(self):
        """Tests run Service method implementation."""
        quantum_circuit = QuantumCircuit(2, 2)
        quantum_circuit.x(0)
        quantum_circuit.cx(0, 1)
        sample_converter = ConversionService(conversion_type="QC_TO_MATRIX")
        result = sample_converter.convert(input_value=quantum_circuit)

        assert_array_equal(result["gate"], [array([[0. + 0.j, 1. + 0.j, 0. + 0.j, 0. + 0.j],
                                                   [1. + 0.j, 0. + 0.j, 0. + 0.j, 0. + 0.j],
                                                   [0. + 0.j, 0. + 0.j, 0. + 0.j, 1. + 0.j],
                                                   [0. + 0.j, 0. + 0.j, 1. + 0.j, 0. + 0.j]]),
                                            array([[1. + 0.j, 0. + 0.j, 0. + 0.j, 0. + 0.j],
                                                   [0. + 0.j, 0. + 0.j, 0. + 0.j, 1. + 0.j],
                                                   [0. + 0.j, 0. + 0.j, 1. + 0.j, 0. + 0.j],
                                                   [0. + 0.j, 1. + 0.j, 0. + 0.j, 0. + 0.j]])])

    def test_qc_to_matrix_gate_raw(self):
        """Tests run Service method implementation."""
        quantum_circuit = QuantumCircuit(2, 2)
        quantum_circuit.x(0)
        quantum_circuit.cx(0, 1)
        sample_converter = ConversionService(conversion_type="QC_TO_MATRIX",
                                             option={"print": "raw"})
        result = sample_converter.convert(input_value=quantum_circuit)

        self.assertEqual(result["gate"], ['\n\n'
                                          '\\begin{bmatrix}\n'
                                          '0 & 1 & 0 & 0  \\\\\n'
                                          ' 1 & 0 & 0 & 0  \\\\\n'
                                          ' 0 & 0 & 0 & 1  \\\\\n'
                                          ' 0 & 0 & 1 & 0  \\\\\n'
                                          ' \\end{bmatrix}\n',
                                          '\n'
                                          '\n'
                                          '\\begin{bmatrix}\n'
                                          '1 & 0 & 0 & 0  \\\\\n'
                                          ' 0 & 0 & 0 & 1  \\\\\n'
                                          ' 0 & 0 & 1 & 0  \\\\\n'
                                          ' 0 & 1 & 0 & 0  \\\\\n'
                                          ' \\end{bmatrix}\n'])

    def test_qc_to_matrix_result_raw(self):
        """Tests run Service method implementation."""
        quantum_circuit = QuantumCircuit(2, 2)
        quantum_circuit.x(0)
        quantum_circuit.cx(0, 1)
        sample_converter = ConversionService(conversion_type="QC_TO_MATRIX",
                                             option={"print": "raw"})
        result = sample_converter.convert(input_value=quantum_circuit)

        self.assertEqual(result["result"], '\n\n'
                                           '\\begin{bmatrix}\n'
                                           '0 & 1 & 0 & 0  \\\\\n'
                                           ' 0 & 0 & 1 & 0  \\\\\n'
                                           ' 0 & 0 & 0 & 1  \\\\\n'
                                           ' 1 & 0 & 0 & 0  \\\\\n'
                                           ' \\end{bmatrix}\n')

    def test_qc_to_matrix_name(self):
        """Tests run Service method implementation."""
        quantum_circuit = QuantumCircuit(2, 2)
        quantum_circuit.x(0)
        quantum_circuit.cx(0, 1)
        sample_converter = ConversionService(conversion_type="QC_TO_MATRIX")
        result = sample_converter.convert(input_value=quantum_circuit)

        self.assertEqual(result["name"], [(0, ['I_{q1}', 'X_{q0}']), (1, ['CX_{q0, q1}'])])

    def test_qc_to_matrix_ccx(self):
        """Tests run Service method implementation."""
        quantum_circuit = QuantumCircuit(3, 3)
        quantum_circuit.x(0)
        quantum_circuit.ccx(0, 1, 2)
        sample_converter = ConversionService(conversion_type="QC_TO_MATRIX")
        result = sample_converter.convert(input_value=quantum_circuit)

        self.assertEqual(result["name"],
                         [(0, ['I_{q2}', 'I_{q1}', 'X_{q0}']), (1, ['CCX_{q0, q1, q2}'])])

    def test_qc_to_matrix_result(self):
        """Tests run Service method implementation."""
        quantum_circuit = QuantumCircuit(2, 2)
        quantum_circuit.x(0)
        quantum_circuit.cx(0, 1)
        sample_converter = ConversionService(conversion_type="QC_TO_MATRIX")
        result = sample_converter.convert(input_value=quantum_circuit)

        assert_array_equal(result["result"].astype(int), array([[0, 1, 0, 0],
                                                                [0, 0, 1, 0],
                                                                [0, 0, 0, 1],
                                                                [1, 0, 0, 0]]))
