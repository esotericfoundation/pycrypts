#!/bin/bash
# Builds this project into a Python package.

set -e

cd "$(dirname "$0")/.." || exit

python3 -m build

cd - || exit
