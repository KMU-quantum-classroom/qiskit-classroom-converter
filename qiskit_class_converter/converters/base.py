"""
Base Converter
"""
from abc import ABC, abstractmethod

import qiskit
from loguru import logger


class BaseConverter(ABC):
    """
    Converter class
    """

    def __init__(self):
        """
        BaseConverter init value
        """
        self.input_value = None
        self.qiskit = qiskit
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
