"""
QuantumCircuit to Bra-ket Notation Converter
"""
from loguru import logger
from sympy import SympifyError
from sympy.parsing.latex import parse_latex

from qiskit_class_converter.converters.base import BaseConverter


class QuantumCircuitToBraketNotationConverter(BaseConverter):
    """
    Converter class
    """

    def actual_convert_action(self):
        self.logger.debug("quantum circuit to bra-ket notation")
        self.input_value.save_statevector()
        result = self.qiskit_aer.AerSimulator().run(self.input_value).result()
        source = result.get_statevector().draw("latex_source")
        try:
            if self.option.get("print", False) == "raw":
                return str(source)
            return str(parse_latex(source))
        except SympifyError:
            # case : 01>
            logger.warning("It caught a SympifyError, so it outputs source text.")
            return source
