#!/bin/bash
# Builds this project into a Python package.

cd "$(dirname "$0")/.." || exit

python3 -m build

pyinstaller -y --add-data "./pycrypt/assets/:./assets/" ./pycrypt/game.py

cd - || exit
