"""
Bra-ket Notation to Matrix Converter
"""
from sympy.parsing.sympy_parser import parse_expr
from sympy import expand
from sympy.parsing.latex import parse_latex

from qiskit_class_converter.converters.base import BaseConverter


class BraketNotationToMatrixConverter(BaseConverter):
    """
    Converter class
    """
    def actual_convert_action(self):
        self.logger.debug("bra-ket notation to matrix")
        self.logger.debug(self.input_value)
        expr = expand(parse_latex(self.input_value))
        self.logger.debug(expr.args)
        
        return self.input_value
    