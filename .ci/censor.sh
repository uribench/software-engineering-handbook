#!/usr/bin/env bash
grep -Rin --color -f blacklist.txt ../Guides ../Topics ../config

if [[ $? == 0 ]]; then
  echo "FAIL: There are some blacklisted words in the repository"
  exit 9
else
  echo "PASS: There are no known blacklisted words in the repository"
  exit 0
fi
