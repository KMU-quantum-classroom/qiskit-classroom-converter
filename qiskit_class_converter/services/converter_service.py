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
    QC_TO_BRA_KET = QuantumCircuitToBraketNotationConverter
    """```python
from qiskit import QuantumCircuit
from qiskit_class_converter import ConversionService

quantum_circuit = QuantumCircuit(2, 2)
quantum_circuit.x(0)
quantum_circuit.cx(0, 1)
sample_converter = ConversionService(conversion_type="QC_TO_BRA_KET")
result = sample_converter.convert(input_value=quantum_circuit)
```"""
    QC_TO_MATRIX = QuantumCircuitToMatrixConverter
    """```python
from qiskit import QuantumCircuit
from qiskit_class_converter import ConversionService

quantum_circuit = QuantumCircuit(2, 2)
quantum_circuit.x(0)
quantum_circuit.cx(0, 1)
sample_converter = ConversionService(conversion_type="QC_TO_MATRIX")
result = sample_converter.convert(input_value=quantum_circuit)
```"""
    MATRIX_TO_QC = MatrixToQuantumCircuitConverter
    """```python
from qiskit import QuantumCircuit
from qiskit_class_converter import ConversionService

input_value = [
    [1, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0]
]
sample_converter = ConversionService(conversion_type="MATRIX_TO_QC")
result = sample_converter.convert(input_value=input_value)
# using user's QuantumCircuit object
quantum_circuit = QuantumCircuit(2, 2)
quantum_circuit.append(result, [0, 1])
```"""
    BRA_KET_TO_MATRIX = BraketNotationToMatrixConverter
    """```python
from qiskit import QuantumCircuit
from qiskit_class_converter import ConversionService

sample_converter = ConversionService(conversion_type="BRA_KET_TO_MATRIX")
sample_converter.convert(input_value="|01>")
```"""


class ConversionService:  # pylint: disable=too-few-public-methods
    """
    Conversion Service class

```python
from qiskit_class_converter import ConversionService

ConversionService(conversion_type="QC_TO_BRA_KET", option={"expression": "simplify"})
```
    """

    def __init__(self, conversion_type: typing.Union[str, ConversionType], option=None):
        """
        init function
        :param conversion_type:  QC_TO_BRA_KET, QC_TO_MATRIX, MATRIX_TO_QC, BRA_KET_TO_MATRIX, BRA_KET_TO_QC
        :param option: See the Options table in this article.
        """
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

            result = sample_converter.convert(input_value=quantum_circuit)
            logger.info(result)

        :param input_value: QuantumCircuit or MATRIX or BRA_KET String
        :return: Converted result
        """
        convert = self.__conversion_object(self.option).convert(input_value)
        return convert
