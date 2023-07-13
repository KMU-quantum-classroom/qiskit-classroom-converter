"""
Bra-ket Notation to Matrix Converter
"""
from sympy.parsing.sympy_parser import parse_expr
from sympy import expand
from sympy.parsing.latex import parse_latex
from sympy.physics.quantum import Bra,Ket
import re

from qiskit_class_converter.converters.base import BaseConverter


class BraketNotationToMatrixConverter(BaseConverter):

    """
    Converter class
    """
   
    def parse_braket(self):
        # result must sympy 
        regex = re.compile("(?=(?P<bra>[<][01]+[|]))|(?=(?P<ket>[|][01]+[>]))|(?=(?P<symbol>[+-]))")
        extr = re.compile("[01]+")
        exprs = regex.findall("|00>+|11>")
        symbols = []
        for expr in exprs :
            #케이스에 따른 expr 처리
            if expr[0] != "":
                val = extr.search(expr[0]).group()
                # val = int(val)
                symbols.append(Bra(val))
            elif expr[1] != "":
                val = extr.search(expr[1]).group()
                # val = int(val)
                symbols.append(Ket(val))
            else : continue # making process
        print(symbols)

    
    def actual_convert_action(self):
        # self.logger.debug("bra-ket notation to matrix")
        # self.logger.debug(self.input_value)
        # expr = expand(parse_latex(self.input_value))
        # self.logger.debug(expr.args)
        
        self.parse_braket()
        return self.input_value
    