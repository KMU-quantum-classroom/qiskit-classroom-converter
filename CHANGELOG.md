# CHANGELOG.md

## 0.4.0 (2023-10-05)

Features :

* Add feature to show the direction of gate (X, CX, CCX, etc...)
* Remove final measurements on circuit
* Add Identity gate to name list
* Change gate name to be uppercase

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