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
from typing import List

import numpy as np
from qiskit import QuantumCircuit
from qiskit.visualization import array_to_latex

from qiskit_class_converter.converters.base import BaseConverter


class QuantumCircuitToMatrixConverter(BaseConverter):
    """
    Converter class
    """

    def actual_convert_action(self):
        self.logger.debug("quantum circuit to matrix")
        gate_list = [self.input_value.data[i][0].name
                     for i in range(len(self.input_value.data))]
        matrix_list = {"gate": [], "name": gate_list}
        # type validate
        if isinstance(self.input_value, (List, QuantumCircuit)):
            dag = self.qiskit.converters.circuit_to_dag(self.input_value)
        else:
            raise TypeError("QuantumCircuit is required.")
        for layer in dag.layers():
            circuit = self.qiskit.converters.dag_to_circuit(layer['graph'])
            matrix_list["gate"].append(self.qiskit.quantum_info.Operator(circuit).to_matrix())
        matrix_list["result"] = self.qiskit.quantum_info.Operator(self.input_value).to_matrix()
        if self.option.get("print", False) == "raw":
            latex_source_list = {"gate": [], "name": gate_list}
            for each_matrix in matrix_list["gate"]:
                latex_source_list["gate"].append(
                    array_to_latex(array=np.array(each_matrix), source=True))
            latex_source_list["result"] = array_to_latex(
                array=np.array(matrix_list["result"]), source=True)
            return latex_source_list
        return matrix_list
