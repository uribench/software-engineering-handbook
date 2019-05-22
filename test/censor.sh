#!/usr/bin/env bash

usage() {
  CMD_NAME="./censor.sh"

  printf "Usage:\n"
  printf "  %s -h|--help|help\n" "$CMD_NAME"
  printf "    Show this message\n\n"
  printf "  %s -v|--version|version\n" "$CMD_NAME"
  printf "    Show version number\n\n"
  printf "  %s BLACKLIST [FILE]...\n" "$CMD_NAME"
  printf "    Example: %s blacklist.txt .\n" "$CMD_NAME"
}

use_encrypted_blacklist() {
  tempblacklist=/tmp/blacklist.txt
  gpg2 --batch --passphrase="$BLACKLIST_PASSWORD" -d "$blacklist" > $tempblacklist
  blacklist=$tempblacklist

  trap on_exit EXIT
}

on_exit() {
  rm -f $tempblacklist
}

check_blacklisted_words() {
  grep -Rinw --color -f $blacklist "${folders[@]}" 

  if [[ $? == 0 ]]; then
    echo "FAIL: There are some blacklisted words in the repository"
    exit 9
  else
    echo "PASS: There are no known blacklisted words in the repository"
    exit 0
  fi
}

censor() {
  blacklist=$1
  shift
  folders=("$@")  # parentheses are needed to store the positional parameters in an array.
                  # later it will be used in 'grep' using array expansion syntax

  if [[ -z ${folders[*]} ]]; then
    usage
    exit 1
  fi

  if [[ $blacklist == *.gpg ]]; then
    use_encrypted_blacklist
  fi

  check_blacklisted_words
}

run() {
  NO_ARGS=0
  if [ $# -eq "$NO_ARGS" ]; then
    usage
    exit 1
  fi

  case "$1" in
    -h | --help    | help    ) usage; exit 0 ;;
    -v | --version | version ) echo "$VERSION"; exit 0 ;;
    * ) censor "$@" ;;
  esac  
}

initialize() {
  VERSION="0.2.0"
  set -u          # '-e' option is not used since 'grep' returns 1 when nothing is found
}

main() {
  initialize
  run "$@"
}

main "$@"
