# Search for Blacklisted Words in the Handbook

## Blacklisting

Put all the blacklisted words in the `./.ci/blacklist.tx` file. Each word has to be placed in a separate line, as `grep` takes the whole line for pattern match.

## Execution

Run the `censor.sh` script as follows:

```bash
$ ./.ci/censor.sh ./.ci/blacklist.txt Guides Topics config
```

Note:

There is no need to include the `Handbook` folder as a target for the search, as it is generated automatically from the contents in the `config` folder and includes only `index.md` files with references to the contents in the `Guides` and `Topics` folders.

## Testing

Two test files were provided:

- pass-example.md
- fail-example.md

The following command should pass:

```bash
./.ci/censor.sh ./.ci/blacklist.txt ./.ci/tests/pass-example.md

# Example Output:
PASS: There are no known blacklisted words in the repository
```

The following command should fail:

```bash
./.ci/censor.sh ./.ci/blacklist.txt ./.ci/tests/fail-example.md

# Example Output:
3:Philips philips PHILIPS john.dow@philips.com
FAIL: There are some blacklisted words in the repository
```
