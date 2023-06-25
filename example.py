import warnings

from loguru import logger
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

from qiskit_class_converter import ConversionService, ConversionType

warnings.filterwarnings('ignore')

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
logger.info("\n" + str(result["result"].astype(int)))

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

# Work In progress
sample_converter = ConversionService(conversion_type="BRA_KET_TO_MATRIX")
sample_converter.convert(input_value="|1>")

sample_converter = ConversionService(conversion_type="BRA_KET_TO_QC")
sample_converter.convert(input_value="|1>")

# Alternatives (using Enum)
sample_converter = ConversionService(conversion_type=ConversionType.BRA_KET_TO_MATRIX)
sample_converter.convert(input_value="|1>")
