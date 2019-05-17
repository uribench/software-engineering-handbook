#!/usr/bin/env bash

BLACKLIST=$1

for FILE in "${@:2}"
do
  grep -Rin --color -f $BLACKLIST $FILE

  if [[ $? == 0 ]]; then
    echo "FAIL: There are some blacklisted words in the repository"
    exit 9
  else
    echo "PASS: There are no known blacklisted words in the repository"
    exit 0
  fi
done

