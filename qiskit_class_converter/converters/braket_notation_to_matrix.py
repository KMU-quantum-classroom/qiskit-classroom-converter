"""
Bra-ket Notation to Matrix Converter
"""
from sympy.parsing.sympy_parser import parse_expr
from sympy import expand
from sympy.parsing.latex import parse_latex
from sympy.physics.quantum import Bra,Ket
from sympy import symbols, Eq, solve, sympify
import re

from qiskit_class_converter.converters.base import BaseConverter


class BraketNotationToMatrixConverter(BaseConverter):

    """
    Converter class
    """
   
    def parse_braket(self):
        # result must sympy 
        #detect bra, ket, sign, cant detect sign but plus, minus can 
        regex = re.compile("(?=(?P<bra>[<][01]+[|]))|(?=(?P<ket>[|][01]+[>]))|(?=(?P<symbol>[+-]))")
        extr = re.compile("[01]+")
        exprs = regex.findall("(sqrt(2)/2)*|00> + (sqrt(2)/2)*|11>")
        symbol = []
        result = None
        for expr in exprs :
            #케이스에 따른 expr 처리
            #ver.1 simple expr
            #Bra
            if expr[0] != "":
                val = extr.search(expr[0]).group()
                # val = int(val)
                symbol.append(Bra(val))
            #Ket
            elif expr[1] != "":
                val = extr.search(expr[1]).group()
                # val = int(val)
                symbol.append(Ket(val))

        result = parse_expr("(sqrt(2)/2)*x + (sqrt(2)/2)*y", evaluate=False, transformations='all', local_dict={'x': symbol[0], 'y': symbol[1]})
        print(result)

    
    def actual_convert_action(self):
        # self.logger.debug("bra-ket notation to matrix")
        # self.logger.debug(self.input_value)
        # expr = expand(parse_latex(self.input_value))
        # self.logger.debug(expr.args)
        
        self.parse_braket()
        return self.input_value
    