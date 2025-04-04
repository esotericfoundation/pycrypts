#!/bin/bash
# Builds this project into an executable.

set -e

cd "$(dirname "$0")/.." || exit

pyinstaller -y --onefile --add-data "./pycrypts/assets:pycrypts/assets" --name pycrypts ./pycrypts/__main__.py

cd - || exit
