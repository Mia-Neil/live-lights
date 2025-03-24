#!/bin/sh

#Set path for AWS CLI
export PATH=/usr/local/bin:$PATH
source ~/.bash_profile

clear
# python3 game_info.py
python3 govee.py
# SCHOOL_NAME=$1
# TEAM=$2
# X={'"'School'"':'"'$SCHOOL_NAME'"','"'Team'"':'"'$TEAM'"'}

# python3 -c "import get_roster; get_roster.get_roster(True, '${TEAM}', '${SCHOOL_NAME}')"

# python3 -c "import get_roster; get_roster.get_roster(True, 'wag', 'Gustavus Adolphus')"
