# qiskit-classroom-converter
Qiskit classroom Converter

## Support convert method

* quantum circuit to bra-ket notation
* quantum circuit to matrix
* matrix to quantum circuit
* bra-ket notation to matrix

---

## Options

| convert method    | option                                   |
|-------------------|------------------------------------------|
| QC_TO_BRA_KET     | expression{simplify, expand}, print{raw} |
| QC_TO_MATRIX      | -                                        |
| MATRIX_TO_QC      | label{str}                               |
| BRA_KET_TO_MATRIX | -                                        |

```python
from qiskit_class_converter import ConversionService

ConversionService(conversion_type="QC_TO_BRA_KET", option={"expression": "simplify"})
```

## Required data

* MATRIX_TO_QC
  * User's QuantumCircuit object

```python
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
```

## How to Install

```bash
pip install qiskit-classroom-converter
```

## Dependencies

* qiskit

## Usage

```python
from qiskit import QuantumCircuit
from qiskit_class_converter import ConversionService
# quantum circuit to matrix
quantum_circuit = QuantumCircuit(2, 2)
quantum_circuit.x(0)
quantum_circuit.cx(0, 1)
sample_converter = ConversionService(conversion_type="QC_TO_MATRIX")
result = sample_converter.convert(input_value=quantum_circuit)
```

code : [example.py](example.py)

## How to test the software

```shell
python -m unittest -v
```

or 

```shell
tox
```
