[![Build Status](https://travis-ci.com/uribench/software-engineering-handbook.svg?branch=master)](https://travis-ci.com/uribench/software-engineering-handbook)

# Test

The tests included in this repository are currently checking the following things:

- [Search for blacklisted words in the Handbook](#search-for-blacklisted-words-in-the-handbook)

## Test Execution

The tests can be executed locally using:

```bash
$ cd test
$ ./test.sh
```

They are also executed automatically on the build server (e.g., Travis-CI) when changes are committed to GitHub or when a Pull Request is created.

## Search for Blacklisted Words in the Handbook

This test is based on the `censor.sh` script from the [uribench/censor][1] GitHub repo.

For details on the `censor.sh` script and how to maintain the blacklist file see the [README][2] file of the [uribench/censor][1] GitHub repo.

---

[1]: https://github.com/uribench/censor
[2]: https://github.com/uribench/censor/blob/master/README.md
