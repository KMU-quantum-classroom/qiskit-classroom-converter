"""
Bra-ket Notation to Matrix Converter
"""
import re
from sympy.parsing.sympy_parser import parse_expr
from sympy.physics.quantum.dagger import Dagger
from sympy.physics.quantum.qubit import Qubit #, measure_all
# from sympy.physics.quantum.represent import represent
from qiskit_class_converter.converters.base import BaseConverter


class BraketNotationToMatrixConverter(BaseConverter):
    """
    Converter class
    """

    # bra-ket regex
    regex_pattern = r"(?P<braket>[<][01]+[|][01]+[>])|(?P<ketbra>[|][01]+[>][<][01]+[|])|(?P<bra>[<][01]+[|])|(?P<ket>[|][01]+[>])"
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

    def make_qubit(self, symbol, isDagger = False):
        """
        make qubit expression
        :return:
        """

        temp = self.extr.search(symbol).group()
        result = Qubit(temp)
        if isDagger :
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
                qubit = self.make_pair(val)
            elif symbol[2] != "": #bra
                val = symbol[2]
                qubit = self.make_qubit(val, isDagger = True)
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
        # expr = self.parse_braket("|01><11|")
        self.logger.info(expr)
        return expr
    