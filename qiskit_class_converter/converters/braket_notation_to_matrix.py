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
        regex_pattern = "(?=(?P<bra>[<][01]+[|]))|(?=(?P<ket>[|][01]+[>]))|(?=(?P<symbol>[+-]))"
        extr = re.compile("[01]+")
        
        expr_str = "(sqrt(2)/2)*|00> + (sqrt(2)/2)*|11>"
        expr_symbols = re.findall(regex_pattern, expr_str)
        dict_num = 97
        local_dict_str = {}
        local_dict ={}
        for symbol in expr_symbols :
            #케이스에 따른 expr 처리
            #ver.1 simple expr
            #Bra
            if symbol[0] != "":
                val = extr.search(symbol[0]).group()
                # val = int(val)
                local_dict_str[chr(dict_num)] = symbol[0]
                local_dict[chr(dict_num)] = (Bra(val))
                dict_num += 1
            #Ket
            elif symbol[1] != "":
                val = extr.search(symbol[1]).group()
                # val = int(val)
                local_dict_str[chr(dict_num)] = symbol[1]
                local_dict[chr(dict_num)] = (Ket(val))
                dict_num += 1
            #bra-ket

        for key in local_dict.keys():
            expr_str = expr_str.replace(local_dict_str[key], key,1)
        expr = parse_expr(expr_str, evaluate=False, transformations='all', local_dict=local_dict)
        print(expr)
        return expr
    
    def actual_convert_action(self):
        # self.logger.debug("bra-ket notation to matrix")
        # self.logger.debug(self.input_value)
        # expr = expand(parse_latex(self.input_value))
        # self.logger.debug(expr.args)
        
        self.parse_braket()
        return self.input_value
    