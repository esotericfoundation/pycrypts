#!/bin/bash
# Builds this project into an executable.

set -e

cd "$(dirname "$0")/.." || exit 1

inkscape "./pycrypts/assets/images/entities/living/monsters/zombie.svg" -o "./pycrypts/assets/images/entities/living/monsters/zombie.png" --export-width=512 --export-height=512
inkscape "./pycrypts/assets/images/entities/helmet.svg" -o "./pycrypts/assets/images/entities/helmet.png" --export-width=512 --export-height=512

pyinstaller -y --onefile --add-data "./pycrypts/assets:pycrypts/assets" --name pycrypts ./pycrypts/__main__.py

cd - || exit 1
