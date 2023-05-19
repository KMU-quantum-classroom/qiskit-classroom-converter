"""
QuantumCircuit to Matrix Converter
"""
from loguru import logger

from qiskit_class_converter.converters.base import BaseConverter


class QuantumCircuitToMatrixConverter(BaseConverter):
    """
    Converter class
    """
    def actual_convert_action(self):
        logger.info("quantum circuit -> matrix")
