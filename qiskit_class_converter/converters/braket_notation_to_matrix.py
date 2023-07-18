"""
Bra-ket Notation to Matrix Converter
"""
import re
from sympy.parsing.sympy_parser import parse_expr
from sympy.physics.quantum.dagger import Dagger
from sympy.physics.quantum.qubit import Qubit, measure_all
from sympy.physics.quantum.represent import represent
from qiskit_class_converter.converters.base import BaseConverter


class BraketNotationToMatrixConverter(BaseConverter):
    """
    Converter class
    """

    # bra-ket 검출 정규 표현식
    regex_pattern = r"(?P<braket>[<][01]+[|][01]+[>])|(?P<bra>[<][01]+[|])|(?P<ket>[|][01]+[>])"

    def parse_braket(self, expr_str):
        """
        detect bra-ket expression to sympy symbols
        :return:
        """
        extr = re.compile("[01]+")
        expr_symbols = re.findall(self.regex_pattern, expr_str)

        local_dict_str = {}
        local_dict ={}

        dict_num = 97
        for symbol in expr_symbols :
            if symbol[0] != "": #bra-ket
                val = symbol[0]
                local_dict_str[chr(dict_num)] = val
                local_dict[chr(dict_num)] = Qubit(extr.search(val).group())
            elif symbol[1] != "": #bra
                val = symbol[1]
                local_dict_str[chr(dict_num)] = val
                local_dict[chr(dict_num)] = Dagger(Qubit(extr.search(val).group()))
            elif symbol[2] != "": #ket
                val = symbol[2]
                local_dict_str[chr(dict_num)] = val
                local_dict[chr(dict_num)] = Qubit(extr.search(val).group())
            dict_num += 1

        for key in local_dict.keys():
            expr_str = expr_str.replace(local_dict_str[key], key,1)
        expr = parse_expr(expr_str, evaluate=False, transformations='all', local_dict=local_dict)
        return expr

    def actual_convert_action(self):
        self.logger.debug("bra-ket notation to matrix")
        self.logger.info(self.input_value)
        expr = self.parse_braket(self.input_value)
        self.logger.info(expr)
        self.logger.info(measure_all(expr))
        self.logger.info(represent(expr))

        # test code - circuit test (CNOT gate)
        # circuit = CNotGate(1, 0)
        # self.logger.info(represent(circuit, nqubits=2))
        return expr
    