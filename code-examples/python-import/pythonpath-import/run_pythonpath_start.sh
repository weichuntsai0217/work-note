#!/bin/bash
# Program: This program runs demo_pythonpath_start.py with a pre-defined PATHONPATH
PYTHONPATH="$(PWD)/mypackages/"
export PYTHONPATH
echo "$PYTHONPATH"
python demo_pythonpath_start.py
