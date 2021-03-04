#!/bin/bash

echo Ubuntu script:

echo Refresh repos...
$(sudo apt update > log.txt 2>&1)

echo Installing Python...
$(sudo apt install python3 >> log.txt 2>&1)

echo Installing pip...
$(sudo apt install python3-pip >> log.txt 2>&1)

echo Installing necessary packages:
$(sudo pip install -r requirements.txt >> log.txt 2>&1)

