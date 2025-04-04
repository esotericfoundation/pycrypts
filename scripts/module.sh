#!/bin/bash
# Builds this project into a Python package.

set -e

cd "$(dirname "$0")/.." || exit 1

python3 -m build

cd - || exit 1
