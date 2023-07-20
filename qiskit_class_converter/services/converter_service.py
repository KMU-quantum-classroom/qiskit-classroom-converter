"""
converter service
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

import typing

from enum import Enum

from qiskit import QuantumCircuit

from qiskit_class_converter.converters.braket_notation_to_matrix \
    import BraketNotationToMatrixConverter
from qiskit_class_converter.converters.braket_notation_to_quantum_circuit \
    import BraketNotationToQuantumCircuitConverter
from qiskit_class_converter.converters.matrix_to_quantum_circuit \
    import MatrixToQuantumCircuitConverter
from qiskit_class_converter.converters.quantum_circuit_to_braket_notation \
    import QuantumCircuitToBraketNotationConverter
from qiskit_class_converter.converters.quantum_circuit_to_matrix \
    import QuantumCircuitToMatrixConverter


class ConversionType(Enum):
    """
    Conversion Type
    """
    BRA_KET_TO_MATRIX = BraketNotationToMatrixConverter
    BRA_KET_TO_QC = BraketNotationToQuantumCircuitConverter
    QC_TO_BRA_KET = QuantumCircuitToBraketNotationConverter
    QC_TO_MATRIX = QuantumCircuitToMatrixConverter
    MATRIX_TO_QC = MatrixToQuantumCircuitConverter


class ConversionService:  # pylint: disable=too-few-public-methods
    """
    Conversion Service class
    """
    def __init__(self, conversion_type: typing.Union[str, ConversionType], option=None):
        if option is None:
            self.option = {}
        self.option = option
        if isinstance(conversion_type, str):
            self.__conversion_object = ConversionType[conversion_type.upper()].value
        elif isinstance(conversion_type, ConversionType):
            self.__conversion_object = conversion_type.value

    def convert(self, input_value: typing.Union[list, QuantumCircuit, str]):
        """
        convert functions
        :param input_value:
        :return:
        """
        convert = self.__conversion_object(self.option).convert(input_value)
        return convert
