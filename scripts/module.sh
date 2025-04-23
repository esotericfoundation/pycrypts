#!/bin/bash
# Builds this project into a Python package.

set -e

cd "$(dirname "$0")/.." || exit 1

inkscape "./pycrypts/assets/images/entities/living/monsters/zombie.svg" -o "./pycrypts/assets/images/entities/living/monsters/zombie.png" --export-width=512 --export-height=512

python3 -m build

cd - || exit 1
