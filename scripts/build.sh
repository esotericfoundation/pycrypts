#!/bin/bash
# Builds this project into an executable.

cd "$(dirname "$0")/.." || exit

pyinstaller -y --onefile --add-data "./pycrypt/assets:pycrypt/assets" --name pycrypt ./pycrypt/__main__.py

cd - || exit
