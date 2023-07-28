"""
Matrix to Quantum Circuit Converter
"""
#  Licensed to the Apache Software Foundation (ASF) under one
#  or more contributor license agreements.  See the NOTICE file
#  distributed with this work for additional information
#  regarding copyright ownership.  The ASF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.

from qiskit_class_converter.converters.base import BaseConverter


class MatrixToQuantumCircuitConverter(BaseConverter):
    """
    Converter class
    """

    def actual_convert_action(self):
        self.logger.debug("matrix to quantum circuit")
        gate = self.qiskit.extensions.UnitaryGate(self.input_value) # parse by unitary circuit. can't describe what circuit is.
        if self.option.get("label", False):
            gate.label = self.option.get("label", "")
        else:
            gate.label = str(self.input_value)
        return gate
