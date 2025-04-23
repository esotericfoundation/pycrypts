#!/bin/bash
# Sets this project up to be run.

set -e

cd "$(dirname "$0")/.." || exit 1

git submodule update --init

python3 -m venv ./venv
source ./venv/bin/activate

pip install -r ./requirements.txt
pip install -r ./requirements-dev.txt

sudo add-apt-repository universe
sudo add-apt-repository ppa:inkscape.dev/stable
sudo apt-get update
sudo apt install inkscape

cd - || exit 1
