#!/bin/bash

for py_file in $(find $YOUR_FOLDER -type f -name "*.py")
do
    python3 $py_file
done
