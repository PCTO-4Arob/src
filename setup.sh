#!/bin/bash

echo Ubuntu script:

echo Refresh repos...
$(sudo apt update > log.txt)

echo Installing Python...
$(sudo apt install python3 >> log.txt)

echo Installing pip...
$(sudo apt install python3-pip >> log.txt)

echo Installing necessary packages:
$(sudo pip install -r requirements.txt)

