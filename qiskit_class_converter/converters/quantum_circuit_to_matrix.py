"""
QuantumCircuit to Matrix Converter
"""
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
