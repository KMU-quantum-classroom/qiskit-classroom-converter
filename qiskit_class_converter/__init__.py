"""Docstring."""
import argparse

from qiskit_class_converter.services.converter_service import ConversionType
from .services.converter_service import ConversionService


def __create_parser():
    parser = argparse.ArgumentParser(description="Conversion Command Line Interface")
    parser.add_argument('converter', type=ConversionType, choices=list(ConversionType))
    parser.add_argument("value", type=str, help="Input value")
    return parser


def run():
    """
    run command
    :return:
    """
    parser = __create_parser()
    args = parser.parse_args()

    system = ConversionService(conversion_type=args.converter)
    result = system.convert(input_value=args.value)
    print("Result:", result)
