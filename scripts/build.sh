#!/bin/bash
# Builds this project into a Python package.

cd "$(dirname "$0")/.." || exit

python3 -m pip install --upgrade build

python3 -m build

pyinstaller -y --add-data "./src/pycrypt/assets/:./assets/" ./src/pycrypt/pycrypt.py
