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
convert class
"""
import unittest
import warnings

from numpy import array
from qiskit import QuantumCircuit
from qiskit.circuit import Instruction
from sympy.physics.quantum.qubit import Qubit
from sympy import sqrt
from sympy.physics.quantum import represent


from qiskit_class_converter.converters.braket_notation_to_matrix \
    import BraketNotationToMatrixConverter
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
        symbol = 1/sqrt(2)*(Qubit('00')+Qubit('11'))
        input_value = "sqrt(2)*|00>/2+sqrt(2)*|11>/2"
        result = main.convert(input_value=input_value)
        self.assertEqual(represent(result), represent(symbol))

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