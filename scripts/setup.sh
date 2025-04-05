#!/bin/bash
# Sets this project up to be run.

set -e

cd "$(dirname "$0")/.." || exit 1

git submodule update --init

python3 -m venv ./venv
source ./venv/bin/activate

pip install -r ./requirements.txt
pip install -r ./requirements-dev.txt

cd - || exit 1
