#!/bin/bash
# Builds this project into a Python package.

cd "$(dirname "$0")/.." || exit

python3 -m build

cd - || exit
