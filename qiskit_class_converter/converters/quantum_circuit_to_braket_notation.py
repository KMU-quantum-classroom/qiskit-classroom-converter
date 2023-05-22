"""
QuantumCircuit to Bra-ket Notation Converter
"""
from qiskit_class_converter.converters.base import BaseConverter


class QuantumCircuitToBraketNotationConverter(BaseConverter):
    """
    Converter class
    """

    def actual_convert_action(self):
        self.logger.debug("quantum circuit to bra-ket notation")
        self.input_value.save_statevector()
        result = self.qiskit_aer.AerSimulator().run(self.input_value).result()
        return result.get_statevector().draw("latex_source")
