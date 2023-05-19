"""
Matrix to Quantum Circuit Converter
"""
from loguru import logger

from qiskit_class_converter.converters.base import BaseConverter


class MatrixToQuantumCircuitConverter(BaseConverter):
    """
    Converter class
    """
    def actual_convert_action(self):
        logger.info("matrix -> quantum circuit")
