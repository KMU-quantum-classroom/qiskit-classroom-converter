# Make new environment and install
python -m venv .flake8-qiskit-migration-venv
source .flake8-qiskit-migration-venv/bin/activate
pip install flake8-qiskit-migration

# Run plugin on Python code
flake8 --select QKT100 ../qiskit_class_converter/*

# Deactivate and delete environment
deactivate
rm -r .flake8-qiskit-migration-venv