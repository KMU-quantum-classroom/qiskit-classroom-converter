# CHANGELOG.md

## 0.6.0 (2025-01-01)

happy new year!

The Version has been updated to be compatible with **Qiskit 1.3.1** and **Python 3.13**.
and drop support for Python 3.9 due to changes support for our dependency.

### major dependencies

- Bump qiskit from 1.1.0 to 1.3.1
- Bump qiskit-aer from 0.14.2 to 0.15.1


## 0.5.1 (2024-06-03)

### dependencies

- Bump qiskit from 1.0.1 to 1.1.0
- Bump qiskit-aer from 0.13.3 to 0.14.2
- and other development dependencies

## 0.5.0 (2024-03-06)

The Version has been updated to be compatible with **Qiskit 1.0.0** and **Python 3.12**.

Qiskit Dependencies:

- **Bump qiskit from 0.45.1 to 1.0.1**
  - changes in Qiskit 1.0.0
  - read the release notes for more information
    - https://docs.quantum.ibm.com/api/qiskit/release-notes/1.0
- Bump qiskit-aer from 0.13.1 to 0.13.3

Other Dependencies:

- Bump numpy from 1.26.2 to 1.26.4
- Bump notebook from 7.0.6 to 7.1.1
- Bump pdoc from 14.1.0 to 14.4.0
- Bump pylint from 3.0.2 to 3.1.0 
- Bump coverage from 7.3.2 to 7.4.3

Changes:

- Updated the QuantumCircuitToMatrixConverter class to be compatible with Qiskit 1.0.0. 
  - The Bit class in Qiskit 1.0.0 no longer has register and index attributes. 
  - The actual_convert_action method of the QuantumCircuitToMatrixConverter class has been updated to use QuantumCircuit.find_bit() instead of directly accessing the index attribute of a Bit object.
- optimized the code to be compatible with qiskit 1.0.0
- added unittest to be compatible with python 3.12

## 0.4.3 (2023-12-02)

Qiskit Dependencies:

- Bump qiskit from 0.45.0 to 0.45.1
- Bump qiskit-aer from 0.13.0 to 0.13.1

Other Dependencies:

- Bump ipython from 8.17.2 to 8.18.1 
- Bump numpy from 1.26.1 to 1.26.2 
- Bump tox from 4.11.3 to 4.11.4 


## 0.4.2 (2023-11-13)

This is Qiskit patch release, updating the qiskit and qiskit-aer Package.

Qiskit Dependencies:

- Bump qiskit from 0.44.2 to 0.45.0 
  - all unparametrized gates in the Qiskit standard circuit library are now singletons.
  - qiskit.extensions will be fully deprecated in a future release, moved to the circuit library.
- Bump qiskit-aer from 0.12.2 to 0.13.0

Other Dependencies:

- Bump ipython from 8.16.1 to 8.17.2
- Bump notebook from 7.0.4 to 7.0.6 
- Bump numpy from 1.26.0 to 1.26.1
- Bump pylint from 3.0.1 to 3.0.2


## 0.4.1 (2023-10-12)

This is small patch release, updating only the Qiskit Package.

Dependencies:

- Bump qiskit from 0.44.1 to 0.44.2
- Bump pylint from 3.0.0 to 3.0.1

## 0.4.0 (2023-10-04)

Features :

* Add feature to show the direction of gate (X, CX, CCX, etc...)
* Remove final measurements on circuit
* Add Identity gate to name list
* Change gate name to be uppercase

Dependencies:

- Bump ipython from 8.15.0 to 8.16.1
- Bump numpy from 1.25.2 to 1.26.0 
- Bump notebook from 7.0.3 to 7.0.4
- Bump pylint from 2.17.5 to 3.0.0
- Bump coverage from 7.3.1 to 7.3.2

## 0.3.0 (2023-09-13)

Features :

- Changed to return gate names per circuit layer when converting to matrix.
  - case : If a lot of qubit and layer 0 has x gate and cx gate.
  - ```[(0, ['x', 'cx'])]```

Dependencies:

- Bump ipython from 8.14.0 to 8.15.0
- Bump notebook from 7.0.2 to 7.0.3
- Bump loguru from 0.7.0 to 0.7.2
- Bump build from 0.10.0 to 1.0.3
- Bump tox from 4.10.0 to 4.11.3
- Bump coverage from 7.3.0 to 7.3.1
- Bump pdoc from 14.0.0 to 14.1.0

## 0.2.0 (2023-08-26)

Features :
- Add the feature to return gate names used when converting from qc to matrix.
  - order is always preserved.
- Add Jupyter notebook dev environment for ARM Mac user

Dependencies:

- Bump coverage from 7.2.7 to 7.3.0
- Bump tox from 4.6.4 to 4.10.0
- Bump qiskit from 0.44.0 to 0.44.1

Remove :
- BRA_KET_TO_MATRIX was removed in 0.2.0.


## 0.1.1 (2023-08-10)

Documentation :
- Add acknowledgement english, korean text

## 0.1.0 (2023-08-06)

Features :
- Add latex visualize feature for matrix & formula
- Add validation code

Fix :
- change BRA_KET_TO_MATRIX to STR_TO_BRA_KET naming

Deprecate :
- BRA_KET_TO_MATRIX was changed to STR_TO_BRA_KET and deprecated.
- drop support for Python 3.8 due to changes support for our dependency.

## 0.0.5 (2023-08-02)

Fix:
- Changed to get the version from the package's metadata.
- Disabled 0.0.4 version.

## ~~0.0.4 (2023-08-02)~~

Features :
- Add version information constant
  - include Converter, Qiskit version

Fix:
- fix error that unnecessarily return value from logger.

## 0.0.3 (2023-07-31)

Fix:

- Preventing automatic discovery in python setuptools.
  - https://setuptools.pypa.io/en/latest/history.html#v61-0-0
- Optimize Python Package

## 0.0.2 (2023-07-30)

Dependencies:

- Bump qiskit from 0.43.2 to 0.44.0
- Bump qiskit-aer from 0.12.1 to 0.12.2
- Bump tox from 4.6.3 to 4.6.4
- Bump pylint from 2.17.4 to 2.17.5

Fix:

- Check the qiskit-aer package and resolve dependencies
- Change description_file syntax required by build system
- Reformat code

## 0.0.1 (2023-07-28)

Features:

- initial release

Fix:

-