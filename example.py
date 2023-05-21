from loguru import logger
from qiskit import QuantumCircuit

from qiskit_class_converter import ConversionService, ConversionType

# matrix to quantum circuit
input_value = [
    [1, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0]
]
sample_converter = ConversionService(conversion_type="MATRIX_TO_QC")
result = sample_converter.convert(input_value=input_value)
quantum_circuit = QuantumCircuit(2)
quantum_circuit.append(result, [0, 1])
logger.info(quantum_circuit)

# quantum circuit to matrix
quantum_circuit = QuantumCircuit(2, 2)
quantum_circuit.cx(0, 1)
sample_converter = ConversionService(conversion_type="QC_TO_MATRIX")
result = sample_converter.convert(input_value=quantum_circuit)
logger.info(result)


# Work In progress
sample_converter = ConversionService(conversion_type="BRA_KET_TO_MATRIX")
sample_converter.convert(input_value="|1>")

sample_converter = ConversionService(conversion_type="BRA_KET_TO_QC")
sample_converter.convert(input_value="|1>")

quantum_circuit = QuantumCircuit(1, 1)
quantum_circuit.h(0)
quantum_circuit.measure([0], [0])
sample_converter = ConversionService(conversion_type="QC_TO_BRA_KET")
sample_converter.convert(input_value=quantum_circuit)

# Alternatives (using Enum)
sample_converter = ConversionService(conversion_type=ConversionType.BRA_KET_TO_MATRIX)
sample_converter.convert(input_value="|1>")
