#!/bin/sh

#Set path for AWS CLI
export PATH=/usr/local/bin:$PATH
source ~/.bash_profile

clear
# python3 game_info.py
python3 govee.py
