# qiskit-classroom-converter
Qiskit classroom Converter

## Support convert method

* bra-ket notation -> matrix
* bra-ket notation -> quantum circuit
* quantum circuit -> bra-ket notation 
* quantum circuit -> matrix 
* matrix -> quantum circuit

---

## Installation

```bash
python3 -m build
pip install .
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

----

[//]: # (## Open source licensing info)
[//]: # (* [LICENSE]&#40;LICENSE&#41;)
