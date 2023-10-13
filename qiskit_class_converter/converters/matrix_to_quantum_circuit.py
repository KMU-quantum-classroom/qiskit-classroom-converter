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
        mat_2bit = None
        with open('./qiskit_class_converter/converters/preset/matrices_1bit.json',
                   encoding='utf-8') as file:
            mat_1bit = json.load(file)

        with open('./qiskit_class_converter/converters/preset/matrices_2bit.json',
                   encoding='utf-8') as file:
            mat_2bit = json.load(file)

        return mat_1bit, mat_2bit

    # 재귀 알고리즘 or 반복문 사용 -> high load
    def make_circuit(self, target, dimension) :
        """
        make_circuit from assumed circuit list -> todo
        """
        return 0

    # matrix 탐색 -> tree 형으로 완전탐색을 기본으로 감.
    def measure_circuit(self, target) :
        """
        assuming circuit -> todo
        """

        mat_1bit, mat_2bit = self.load_matrix_preset()
        target_dimemsion = None
        if isinstance(target, List):
            target_dimemsion = int(np.sqrt(len(target)))
        elif isinstance(target, np.ndarray):
            target_dimemsion = target.ndim

        self.logger.debug(target_dimemsion)

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
