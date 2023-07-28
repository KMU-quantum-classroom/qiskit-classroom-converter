"""
Bra-ket Notation to Matrix Converter
"""
# from sympy.physics.quantum.represent import represent
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

import re
from sympy.parsing.sympy_parser import parse_expr
from sympy.physics.quantum.dagger import Dagger
from sympy.physics.quantum.qubit import Qubit #, measure_all

from qiskit_class_converter.converters.base import BaseConverter


class BraketNotationToMatrixConverter(BaseConverter):
    """
    Converter class
    """

    # bra-ket regex
    regex_pattern = r"(?P<braket>[<][01]+[|][01]+[>])|(?P<ketbra>[|][01]+[>][<][01]+[|])|\
                    (?P<bra>[<][01]+[|])|(?P<ket>[|][01]+[>])"
    extr = re.compile("[01]+")

    def make_pair(self, symbol, reverse = False):
        """
        make multiple qubit expression
        :return:
        """

        temps = self.extr.findall(symbol)

        exp1 = Dagger(Qubit(temps[0]))
        exp2 = Qubit(temps[1])

        if reverse :
            exp1 = Dagger(exp1)
            exp2 = Dagger(exp2)

        return exp1 * exp2

    def make_qubit(self, symbol, is_dagger = False):
        """
        make qubit expression
        :return:
        """

        temp = self.extr.search(symbol).group()
        result = Qubit(temp)
        if is_dagger :
            result = Dagger(result)

        return result

    def create_qubits(self, expr_symbols):
        """
        create qubits using symbols
        :return:
        """

        local_dict_str = {}
        local_dict ={}

        dict_num = 97
        for symbol in expr_symbols :
            val = None
            qubit = None

            if symbol[0] != "": #bra-ket
                val = symbol[0]
                qubit = self.make_pair(val)
            elif symbol[1] != "": #ket-bra
                val = symbol[1]
                qubit = self.make_pair(val, reverse = True)
            elif symbol[2] != "": #bra
                val = symbol[2]
                qubit = self.make_qubit(val, is_dagger = True)
            elif symbol[3] != "": #ket
                val = symbol[3]
                qubit = self.make_qubit(val)

            local_dict_str[chr(dict_num)] = val
            local_dict[chr(dict_num)] = qubit
            dict_num += 1

        return local_dict_str, local_dict

    def parse_braket(self, expr_str):
        """
        detect bra-ket expression to sympy symbols
        :return:
        """
        expr_symbols = re.findall(self.regex_pattern, expr_str)

        local_dict_str, local_dict = self.create_qubits(expr_symbols)

        for key in local_dict:
            expr_str = expr_str.replace(local_dict_str[key], key,1)
        expr = parse_expr(expr_str, evaluate=False, transformations='all', local_dict=local_dict)
        return expr

    def actual_convert_action(self):
        self.logger.debug("bra-ket notation to matrix")
        expr = self.parse_braket(self.input_value)
        self.logger.info(expr)
        return expr
    