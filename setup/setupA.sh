#!/bin/bash

echo Arch-based script:

echo Refresh repos...
$(sudo pacmam -Syyuu > log.txt 2>&1)

echo Installing Python...
$(sudo pacman -S python3 >> log.txt 2>&1)

echo Installing pip...
$(sudo pacman -S python3-pip >> log.txt 2>&1)

echo Installing necessary packages:
$(sudo pip install -r requirements.txt >> log.txt 2>&1)
