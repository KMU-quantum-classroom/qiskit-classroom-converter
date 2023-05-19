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
python setup.py install 
```

## Dependencies

* qiskit

## Usage

```python
from qiskit_class_converter import ConversionService

sample_converter = ConversionService(conversion_type="BRA_KET_TO_MATRIX")
sample_converter.convert(input_value="|1>")
```

code : [example.py](example.py)

or

```shell
qiskit-class-converter BRA_KET_TO_MATRIX "|1>"
```

CLI : ```$ qiskit-class-converter --help```

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
