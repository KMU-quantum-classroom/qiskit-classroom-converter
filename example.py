import warnings

from loguru import logger
from qiskit import QuantumCircuit

from qiskit_class_converter import ConversionService, ConversionType

warnings.filterwarnings('ignore')

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
logger.info("\n" + str(quantum_circuit))

# quantum circuit to matrix
quantum_circuit = QuantumCircuit(2, 2)
quantum_circuit.cx(0, 1)
sample_converter = ConversionService(conversion_type="QC_TO_MATRIX")
result = sample_converter.convert(input_value=quantum_circuit)
logger.info("\n" + str(result.astype(int)))

# quantum circuit to bra-ket
quantum_circuit = QuantumCircuit(2, 2)
quantum_circuit.x(0)
quantum_circuit.cx(0, 1)
sample_converter = ConversionService(conversion_type="QC_TO_BRA_KET")
result = sample_converter.convert(input_value=quantum_circuit)
logger.info(result)

# Work In progress
sample_converter = ConversionService(conversion_type="BRA_KET_TO_MATRIX")
sample_converter.convert(input_value="|1>")

sample_converter = ConversionService(conversion_type="BRA_KET_TO_QC")
sample_converter.convert(input_value="|1>")

# Alternatives (using Enum)
sample_converter = ConversionService(conversion_type=ConversionType.BRA_KET_TO_MATRIX)
sample_converter.convert(input_value="|1>")
