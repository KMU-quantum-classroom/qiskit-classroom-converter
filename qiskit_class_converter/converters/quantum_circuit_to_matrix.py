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

    def __init__(self, option=None):
        super().__init__(option)
        self.__programmable_variable_per_qubit = None

    def insert_i_gate(self):
        """
        Trace empty space in the layer to enter the Identity gate.
        """
        arr = [f"I_{{q{i}}}" for i in range(self.__programmable_variable_per_qubit["total_qubits"])]
        for i in self.__programmable_variable_per_qubit["gate_qubits"]:
            for j in i["qubit"]:
                arr[j] = i["name"]
        arr = list(dict.fromkeys(arr))
        arr.reverse()
        return arr

    def actual_convert_action(self):
        self.logger.debug("quantum circuit to matrix")
        matrix_list = {"gate": [], "name": []}
        # type validate
        if isinstance(self.input_value, (List, QuantumCircuit)):
            self.input_value = self.input_value.remove_final_measurements(inplace=False)
            dag = self.qiskit.converters.circuit_to_dag(self.input_value)
        else:
            raise TypeError("QuantumCircuit is required.")
        layer_index = 0
        for layer in dag.layers():
            circuit = self.qiskit.converters.dag_to_circuit(layer['graph'])
            matrix_list["gate"].append(self.qiskit.quantum_info.Operator(circuit).to_matrix())
            self.__programmable_variable_per_qubit = {"total_qubits": circuit.num_qubits,
                                                      "gate_qubits": []}
            for _inst in circuit.data:
                _inst_upper_name = _inst[0].name.upper()
                if _inst[0].num_qubits == 2:
                    gate_name = (_inst_upper_name +
                                 "_{q" + str(_inst.qubits[0].index) +
                                 ", q" + str(_inst.qubits[1].index) + "}")
                    self.__programmable_variable_per_qubit["gate_qubits"].append(
                        {"name": gate_name,
                         "qubit": [_inst.qubits[0].index, _inst.qubits[1].index]}
                    )
                elif _inst[0].num_qubits == 3:
                    gate_name = (_inst_upper_name +
                                 "_{q" + str(_inst.qubits[0].index) +
                                 ", q" + str(_inst.qubits[1].index) +
                                 ", q" + str(_inst.qubits[2].index) + "}")
                    self.__programmable_variable_per_qubit["gate_qubits"].append(
                        {"name": gate_name,
                         "qubit": [_inst.qubits[0].index,
                                   _inst.qubits[1].index,
                                   _inst.qubits[2].index]}
                    )
                else:
                    gate_name = _inst_upper_name + "_{q" + str(_inst.qubits[0].index) + "}"
                    self.__programmable_variable_per_qubit["gate_qubits"].append(
                        {"name": gate_name, "qubit": [_inst.qubits[0].index]}
                    )
            matrix_list["name"].append((layer_index, self.insert_i_gate()))
            layer_index += 1
        matrix_list["result"] = self.qiskit.quantum_info.Operator(self.input_value).to_matrix()
        if self.option.get("print", False) == "raw":
            latex_source_list = {"gate": [], "name": matrix_list["name"]}
            for each_matrix in matrix_list["gate"]:
                latex_source_list["gate"].append(
                    array_to_latex(array=np.array(each_matrix), source=True))
            latex_source_list["result"] = array_to_latex(
                array=np.array(matrix_list["result"]), source=True)
            return latex_source_list
        return matrix_list
