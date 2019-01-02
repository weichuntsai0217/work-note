#!/bin/bash
# Program: This program runs unit tests with a pre-defined PATHONPATH
PYTHONPATH="$(PWD)/../mypackages/"
export PYTHONPATH
echo "$PYTHONPATH"
python $(PWD)/test_module_x.py
python $(PWD)/test_module_y.py
python $(PWD)/test_module_z.py
