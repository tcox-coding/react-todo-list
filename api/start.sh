#!/bin/bash

# Remove the virtual environment if it exists and create a new one.
[ -d venv ] && rm -r venv
python -m venv venv

# Activate the virtual environment and install the required packages.
source venv/bin/activate

pip install -r requirements.txt