#!/bin/bash
# Sets this project up to be run.

set -e

cd "$(dirname "$0")/.." || exit 1

rm -rf ./venv

git submodule update --init

python3 -m venv ./venv
source ./venv/bin/activate

pip install -r ./requirements.txt
pip install -r ./requirements-dev.txt

sudo add-apt-repository universe || {
  echo "Failed to get repository"
}

sudo add-apt-repository ppa:inkscape.dev/stable || {
  echo "Failed to get repository"
}

sudo apt-get update
sudo apt install inkscape

cd - || exit 1
