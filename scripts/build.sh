#!/bin/bash
# Builds this project into a Python package.

cd "$(dirname "$0")/.." || exit

python3 -m build

pyinstaller -y --onefile --add-data "./pycrypt/assets:pycrypt/assets" ./pycrypt/__main__.py

cd - || exit
