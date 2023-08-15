FROM jupyter/minimal-notebook:python-3.11

LABEL maintainer="minwook shin <minwook0106@gmail.com>"

USER root
COPY qiskit_class_converter .work/qiskit_class_converter/
COPY pyproject.toml .work/pyproject.toml
RUN pip install -e '.work'
COPY qiskit_classroom_converter_public_demo.ipynb \
    ./qiskit_classroom_converter_public_demo.ipynb