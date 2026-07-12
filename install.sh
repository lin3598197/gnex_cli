#!/usr/bin/env/ bash

git clone https://github.com/lin3598197/gnex_cli.git
cd gnex_cli
python3 -m venv .venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
