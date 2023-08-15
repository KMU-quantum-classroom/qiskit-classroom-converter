# qiskit-classroom-converter
Qiskit classroom Converter

## Documents

https://kmu-quantum-classroom.github.io/qiskit-classroom-converter/qiskit_class_converter.html

## Support convert method

* quantum circuit to bra-ket notation
* quantum circuit to matrix
* matrix to quantum circuit
* string to bra-ket notation

---

## Options

| convert method | option                                   |
|----------------|------------------------------------------|
| QC_TO_BRA_KET  | expression{simplify, expand}, print{raw} |
| QC_TO_MATRIX   | print{raw}                               |
| MATRIX_TO_QC   | label{str}                               |
| STR_TO_BRA_KET | print{raw}                               |

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

## ARM Platform

Mac ARM chips users may have issues running this package.

We have provided a Dockerfile, which can be used docker-compose.

```shell
docker-compose up --build
```

## Acknowledgement

- 국문 : "본 연구는 2022년 과학기술정보통신부 및 정보통신기획평가원의 SW중심대학사업의 연구결과로 수행되었음"(2022-0-00964)
- English : "This research was supported by the MIST(Ministry of Science, ICT), Korea, under the National Program for Excellence in SW), supervised by the IITP(Institute of Information & communications Technology Planning & Evaluation) in 2022"(2022-0-00964)
