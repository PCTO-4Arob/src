#!/bin/bash

echo Ubuntu script:

echo Refresh repos...
$(sudo apt update)

echo Installing Python...
$(sudo apt install python3)

echo Installing pip...
$(sudo apt install python3-pip)

echo Installing necessary packages:
$(sudo pip install requirements.txt)

