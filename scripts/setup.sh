#!/bin/bash
# Sets this project up to be run.

set -e

cd "$(dirname "$0")/.." || exit 1

echo "Cleaning up potential old virtual environment"

rm -rf ./venv

echo "Updating submodules"

git submodule update --init

echo "Creating virtual environment"

python3 -m venv ./venv

echo "Entering virtual environment"

source ./venv/bin/activate

echo "Installing dependencies"

pip install -r ./requirements.txt
pip install -r ./requirements-dev.txt

echo "Installing Inkscape"

sudo add-apt-repository universe || {
  echo "Failed to get repository"
}

sudo add-apt-repository ppa:inkscape.dev/stable || {
  echo "Failed to get repository"
}

sudo apt-get update
sudo apt install inkscape

cd - || exit 1
