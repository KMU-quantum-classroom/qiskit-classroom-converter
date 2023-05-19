"""
Bra-ket Notation to QuantumCircuit Converter
"""
from loguru import logger

from qiskit_class_converter.converters.base import BaseConverter


class BraketNotationToQuantumCircuitConverter(BaseConverter):
    """
    Converter class
    """
    def actual_convert_action(self):
        logger.info("bra-ket notation -> quantum circuit")
