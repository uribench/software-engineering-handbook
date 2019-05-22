#!/usr/bin/env bash

if [[ ! -f censor.sh ]]; then
  wget "https://raw.githubusercontent.com/uribench/censor/master/censor.sh"
  chmod +x censor.sh
fi

./censor.sh blacklist.txt.gpg ../Guides/ ../Topics/ ../config/