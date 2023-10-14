"""
Matrix to Quantum Circuit Converter
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
import json
import os
from qiskit_class_converter.converters.base import BaseConverter


class MatrixToQuantumCircuitConverter(BaseConverter):
    """
    Converter class
    """

    def load_matrix_preset(self):
        """
        load matrix preset
        """
        mat_1bit = None
        with open('./qiskit_class_converter/converters/preset/matrices_1bit.json',
                   encoding='utf-8') as file:
            mat_1bit = json.load(file)
        with open('./qiskit_class_converter/converters/preset/matrices_2bit.json',
                   encoding='utf-8') as file:
            mat_2bit = json.load(file)

        return mat_1bit, mat_2bit


    def make_circuit(self, target, dimension) :
        """
        make_circuit from assumed circuit list -> todo
        """
        return 0

    def matching_circuit(self, target, qubits, result):

        # 실행시간 -> big O(preset_time^n)
        mat_1bit, mat_2bit = self.load_matrix_preset()
        size_1bit = len(mat_1bit["matrices"])
        size_2bit = len(mat_2bit["matrices"])
        
        
        for i in range(pow((size_1bit+size_2bit), qubits)):
            product = None
                
        return result

    def combine_circuit(self, target, size):
        """
        combine possible circuit list -todo
        """
        result = []

        #checking qubit size
        qubits = 0
        while size > 1:
            size /= 2
            qubits += 1

        self.logger.debug(f"num of qubits : {qubits}")

        # making kroneker product
        # it should be {q_n, q_n-1, q_n-2 ... q_0}

        # maybe it's ok to make brute froce search function
        
        return result

    # matrix 탐색 -> tree 형으로 완전탐색을 기본으로 감.
    def measure_circuit(self, target) :
        """
        assuming circuit -> todo
        """

        #get matrix size -> checking size is too large
        target_size = None
        if isinstance(target, List) :
            target = np.asarray(target)

        target_size = int(np.sqrt(target.size))

        self.logger.debug(f"array size : {target_size}")

        #checking size
        #2, 4, 8 size is only accepted dimension
        if target_size > 8 :
            raise ValueError("dimension is too large please input ")
        if target_size % 2 != 0 and target_size == 6:
            raise ValueError("invalid size")

        result = self.combine_circuit(target, target_size)

        return 0

    def actual_convert_action(self):
        self.logger.debug("matrix to quantum circuit")
        # type validate
        if isinstance(self.input_value, (List, np.ndarray)):
            self.measure_circuit(self.input_value)
            gate = self.qiskit.extensions.UnitaryGate(self.input_value)
        else:
            raise TypeError("List or np.ndarray is required.")
        # parse by unitary circuit. can't describe what circuit is.
        if self.option.get("label", False):
            gate.label = self.option.get("label", "")
        else:
            gate.label = str(self.input_value)
        return gate
