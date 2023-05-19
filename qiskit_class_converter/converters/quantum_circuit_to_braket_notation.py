"""
QuantumCircuit to Bra-ket Notation Converter
"""
from loguru import logger

from qiskit_class_converter.converters.base import BaseConverter


class QuantumCircuitToBraketNotationConverter(BaseConverter):
    """
    Converter class
    """
    def actual_convert_action(self):
        logger.info("quantum circuit -> bra-ket notation")
