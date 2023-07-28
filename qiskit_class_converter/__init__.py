"""
# qiskit-classroom-converter API Documents

Convert quantum circuits, matrices, and bra-ket strings.

# How to Install

```
pip install qiskit-classroom-converter
```

# Support convert method

* quantum circuit to bra-ket notation
* quantum circuit to matrix
* matrix to quantum circuit
* bra-ket notation to matrix

# Options

| convert method    | option                                   |
|-------------------|------------------------------------------|
| QC_TO_BRA_KET     | expression{simplify, expand}, print{raw} |
| QC_TO_MATRIX      | -                                        |
| MATRIX_TO_QC      | label{str}                               |
| BRA_KET_TO_MATRIX | -                                        |

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

from .services.converter_service import ConversionService, ConversionType

__all__ = [ConversionService, ConversionType]
