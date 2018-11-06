#!/bin/bash

python3 setup.py sdist bdist_wheel
pip3 install dist/yutil-0.1.tar.gz
