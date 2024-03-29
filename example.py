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

import warnings

from loguru import logger
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

from qiskit_class_converter import ConversionService, ConversionType, __FULL_VERSION__, \
    __LICENSE__, __acknowledgement_en__

warnings.filterwarnings('ignore')

version = __FULL_VERSION__
logger.info(version)

LICENSE = __LICENSE__
logger.info(LICENSE)

logger.info(__acknowledgement_en__)

# matrix to quantum circuit
input_value = [
    [1, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0]
]
sample_converter = ConversionService(conversion_type="MATRIX_TO_QC", option={"label": "CX gate"})
result = sample_converter.convert(input_value=input_value)
quantum_circuit = QuantumCircuit(2, 2)
quantum_circuit.x(0)
quantum_circuit.append(result, [0, 1])
quantum_circuit.measure(range(2), range(2))
backend = AerSimulator()
qc_compiled = transpile(quantum_circuit, backend)
counts = backend.run(qc_compiled).result().get_counts()
logger.info("\n" + str(quantum_circuit))
logger.info(counts)

# quantum circuit to matrix
quantum_circuit = QuantumCircuit(2, 2)
quantum_circuit.x(0)
quantum_circuit.cx(0, 1)
sample_converter = ConversionService(conversion_type="QC_TO_MATRIX")
result = sample_converter.convert(input_value=quantum_circuit)
for gate in result["gate"]:
    logger.info("\n" + str(gate.astype(int)))
logger.info("list: " + str(result["name"]))
logger.info("\n" + str(result["result"].astype(int)))

# quantum circuit to matrix (for print: raw option)
quantum_circuit = QuantumCircuit(2, 2)
quantum_circuit.x(0)
quantum_circuit.cx(0, 1)
sample_converter = ConversionService(conversion_type="QC_TO_MATRIX", option={"print": "raw"})
result = sample_converter.convert(input_value=quantum_circuit)
for gate in result["gate"]:
    logger.info(gate)
logger.info(result["result"])

# quantum circuit to bra-ket
quantum_circuit = QuantumCircuit(2, 2)
quantum_circuit.h(0)
quantum_circuit.x(0)
quantum_circuit.cx(0, 1)
sample_converter = ConversionService(conversion_type="QC_TO_BRA_KET")
result = sample_converter.convert(input_value=quantum_circuit)
logger.info(result)

# quantum circuit to simplify bra-ket
quantum_circuit = QuantumCircuit(2, 2)
quantum_circuit.h(0)
quantum_circuit.x(0)
quantum_circuit.cx(0, 1)
sample_converter = ConversionService(conversion_type="QC_TO_BRA_KET", option={"expression": "simplify"})
result = sample_converter.convert(input_value=quantum_circuit)
logger.info(result)

# quantum circuit to expand bra-ket
quantum_circuit = QuantumCircuit(2, 2)
quantum_circuit.h(0)
quantum_circuit.x(0)
quantum_circuit.cx(0, 1)
sample_converter = ConversionService(conversion_type="QC_TO_BRA_KET", option={"expression": "expand"})
result = sample_converter.convert(input_value=quantum_circuit)
logger.info(result)

# using options
quantum_circuit = QuantumCircuit(2, 2)
quantum_circuit.h(0)
quantum_circuit.x(0)
quantum_circuit.cx(0, 1)
sample_converter = ConversionService(conversion_type="QC_TO_BRA_KET", option={"print": "raw"})
result = sample_converter.convert(input_value=quantum_circuit)
logger.info(result)

sample_converter = ConversionService(conversion_type="STR_TO_BRA_KET")
result = sample_converter.convert(input_value="<00|01>")
logger.info(result)

sample_converter = ConversionService(conversion_type="STR_TO_BRA_KET", option={"print": "raw"})
result = sample_converter.convert(input_value="<00|01>")
logger.info(result)

# # Alternatives (using Enum)
sample_converter = ConversionService(conversion_type=ConversionType.STR_TO_BRA_KET)
result = sample_converter.convert(input_value="sqrt(2)*|00>/2+sqrt(2)*|11>/2")
logger.info(result)

sample_converter = ConversionService(conversion_type=ConversionType.STR_TO_BRA_KET, option={"print": "raw"})
result = sample_converter.convert(input_value="sqrt(2)*|00>/2+sqrt(2)*|11>/2")
logger.info(result)
