#!/usr/bin/env bash

cd gnex_cli
python3 -m venv .venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py