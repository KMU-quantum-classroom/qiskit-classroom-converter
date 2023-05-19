"""
Base Converter
"""
from abc import ABC, abstractmethod

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
        self.result = None

    def convert(self, input_value):
        """
        convert main process
        :return:
        """
        self.input_value = input_value
        self.__pre_process()
        self.actual_convert_action()
        return self.__post_process()

    def __pre_process(self):
        """
        prepare process
        :return:
        """
        logger.info(self.input_value)
        return self.input_value

    @abstractmethod
    def actual_convert_action(self):
        """
        actual action
        :return:
        """
        raise NotImplementedError

    def __post_process(self):
        """
        post process
        :return:
        """
        self.result = self.input_value
        logger.info(self.result)
        return self.result
