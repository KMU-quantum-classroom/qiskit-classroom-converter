from qiskit import QuantumCircuit

from qiskit_class_converter import ConversionService, ConversionType

sample_converter = ConversionService(conversion_type="BRA_KET_TO_MATRIX")
sample_converter.convert(input_value="|1>")

sample_converter = ConversionService(conversion_type="BRA_KET_TO_QC")
sample_converter.convert(input_value="|1>")

input_value = [
    [1, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0]
]
sample_converter = ConversionService(conversion_type="MATRIX_TO_QC")
sample_converter.convert(input_value=input_value)

quantum_circuit = QuantumCircuit(1, 1)
quantum_circuit.h(0)
quantum_circuit.measure([0], [0])
sample_converter = ConversionService(conversion_type="QC_TO_BRA_KET")
sample_converter.convert(input_value=quantum_circuit)

quantum_circuit = QuantumCircuit(1, 1)
quantum_circuit.h(0)
quantum_circuit.measure([0], [0])
sample_converter = ConversionService(conversion_type="QC_TO_MATRIX")
sample_converter.convert(input_value=quantum_circuit)

# Alternatives (using Enum)
sample_converter = ConversionService(conversion_type=ConversionType.BRA_KET_TO_MATRIX)
sample_converter.convert(input_value="|1>")
