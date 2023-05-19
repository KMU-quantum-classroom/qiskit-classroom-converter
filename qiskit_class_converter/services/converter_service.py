"""
converter service
"""
import typing

from enum import Enum

from qiskit_class_converter.converters.braket_notation_to_matrix \
    import BraketNotationToMatrixConverter
from qiskit_class_converter.converters.braket_notation_to_quantum_circuit \
    import BraketNotationToQuantumCircuitConverter
from qiskit_class_converter.converters.matrix_to_quantum_circuit \
    import MatrixToQuantumCircuitConverter
from qiskit_class_converter.converters.quantum_circuit_to_braket_notation \
    import QuantumCircuitToBraketNotationConverter
from qiskit_class_converter.converters.quantum_circuit_to_matrix \
    import QuantumCircuitToMatrixConverter


class ConversionType(Enum):
    """
    Conversion Type
    """
    BRA_KET_TO_MATRIX = BraketNotationToMatrixConverter
    BRA_KET_TO_QC = BraketNotationToQuantumCircuitConverter
    QC_TO_BRA_KET = QuantumCircuitToBraketNotationConverter
    QC_TO_MATRIX = QuantumCircuitToMatrixConverter
    MATRIX_TO_QC = MatrixToQuantumCircuitConverter

    def __str__(self):
        return self.name

    @staticmethod
    def from_string(string_value):
        """
        from_string impl
        :param string_value:
        :return:
        """
        try:
            return ConversionType[string_value]
        except KeyError as exception:
            raise ValueError(exception) from exception


class ConversionService:  # pylint: disable=too-few-public-methods
    """
    Conversion Service class
    """
    def __init__(self, conversion_type: typing.Union[str, ConversionType]):
        print(conversion_type)
        if isinstance(conversion_type, str):
            self.__conversion_object = ConversionType[conversion_type.upper()].value
        elif isinstance(conversion_type, ConversionType):
            self.__conversion_object = conversion_type.value

    def convert(self, input_value):
        """
        convert functions
        :param input_value:
        :return:
        """
        convert = self.__conversion_object().convert(input_value)
        return convert
