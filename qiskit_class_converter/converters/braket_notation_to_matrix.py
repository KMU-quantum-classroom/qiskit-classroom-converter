"""
Bra-ket Notation to Matrix Converter
"""
from loguru import logger

from qiskit_class_converter.converters.base import BaseConverter


class BraketNotationToMatrixConverter(BaseConverter):
    """
    Converter class
    """
    def actual_convert_action(self):
        logger.info("bra-ket notation -> matrix")
