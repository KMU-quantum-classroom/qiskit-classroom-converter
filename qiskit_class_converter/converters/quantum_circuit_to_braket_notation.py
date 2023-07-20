"""
QuantumCircuit to Bra-ket Notation Converter
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

from loguru import logger
from sympy import SympifyError, simplify, expand, latex
from sympy.parsing.latex import parse_latex

from qiskit_class_converter.converters.base import BaseConverter


class QuantumCircuitToBraketNotationConverter(BaseConverter):
    """
    Converter class
    """

    # pylint: disable-next = too-many-return-statements
    def actual_convert_action(self):
        self.logger.debug("quantum circuit to bra-ket notation")
        self.input_value.save_statevector()
        result = self.qiskit_aer.AerSimulator().run(self.input_value).result()
        source = result.get_statevector().draw("latex_source")
        try:
            if (self.option.get("expression", False) == "simplify") and \
                    (self.option.get("print", False) == "raw"):
                return latex(simplify(parse_latex(source)))
            if self.option.get("expression", False) == "simplify":
                return str(simplify(parse_latex(source)))
            if (self.option.get("expression", False) == "expand") and \
                    (self.option.get("print", False) == "raw"):
                return latex(expand(parse_latex(source)))
            if self.option.get("expression", False) == "expand":
                return str(expand(parse_latex(source)))
            if self.option.get("print", False) == "raw":
                return str(source)
            return str(parse_latex(source))
        except SympifyError:
            # case : 01>
            logger.warning("It caught a SympifyError, so it outputs source text.")
            return source
