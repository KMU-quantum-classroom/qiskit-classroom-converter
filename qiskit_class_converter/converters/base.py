"""
Base Converter
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

from abc import ABC, abstractmethod

import qiskit
import qiskit_aer
from loguru import logger


class BaseConverter(ABC):
    """
    Converter class
    """

    def __init__(self, option=None):
        """
        BaseConverter init value
        """
        if option is None:
            option = {}
        self.option = option
        self.input_value = None
        self.qiskit = qiskit
        self.qiskit_aer = qiskit_aer
        self.logger = logger

    def convert(self, input_value):
        """
        convert main process
        :return:
        """
        self.input_value = input_value
        return self.actual_convert_action()

    @abstractmethod
    def actual_convert_action(self):
        """
        actual action
        :return:
        """
        raise NotImplementedError
