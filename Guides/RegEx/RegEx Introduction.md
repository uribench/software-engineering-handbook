# RegEx Introduction

Regular expressions (aka, RegEx) are a textual syntax for representing patterns for matching text. Usually such patterns are used for text processing by string searching algorithms for "find" or "find and replace" operations on strings, or for input validation. 

For an elaborated introduction to RegEx see [Regular expression on Wikipedia][1].


## RegEx Cheat Sheets

There are many RegEx cheat sheets available online, such as the [The ABCs of RegEx by DZone][2] or the [Quick-Start: Regex Cheat Sheet by Rex Egg][3].

Following is a very basic RegEx cheat sheet.

### Basic RegEx Cheat Sheet

### Quantifiers

```regex
m*          0 or more m
m+          1 or more m
m?          0 or 1 m
m{2}        Exactly 2 m
m{2,}       2 or more m
m{2,4}      2, 3 or 4 m
```

### Ranges

```regex
.           Any character except new line (\n)
(A|B)       A or B
(...)       Group
[ABC]       Range (A, B or C)
[^ABC]      Not A, B or C
[A-Z]       Character between A and Z, upper case
[0-9]       Number between 0 and 9
[A-Z0-9]    Characters between A and Z, and numbers between 0 and 9
\m          matches the character m literally (case sensitive)
\1          matches the same text as most recently matched by the 1st capturing group
```

### Anchors

```regex
^           Start of line
$           End of line
```

### Character Classes

```regex
\w          Word (a-z, A-Z, 0-9, including _ (underscore))
\W          Non-word
\d          Digit (0-9)
\D          Non-digit
\s          Whitespace
\S          Not whitespace
\b          Match at beginning or end
\B          Do not match at beginning or end
\0          NULL character
\n          New line
```

### Assertions

```regex
m(?=o)      Lookahead, m followed by o (not matching o)
m(?!o)      Negative lookahead, m not followed by o (not matching o)
```

### Special Characters

In the regex flavors discussed in this tutorial, there are 12 characters with special meanings: 

```regex
\           backslash
^           caret
$           dollar sign
.           period or dot
|           vertical bar or pipe symbol
?           question mark
*           asterisk or star
+           plus sign
()          opening and closing parenthesis
[]          opening and closing square bracket
{}          opening and closing curly brace
```

These special characters are often called "metacharacters". Most of them are errors when used alone.

If you want to use any of these characters as a literal in a regex, you need to escape them with a backslash.


## Online Learning Sites

### Interactive Online Tools

Following are several worth mentioning free online RegEx learning sites and interactive consoles for experimenting with RegEx patterns. Most of them provide the same capabilities, including regular expression debugger with real-time explanation, error detection and highlighting. 

Check them to see which one you like better.

[RegEx101][4]

[RegExr][5]

[RegEx Tester][6]

### Language Specific Tutorials

[Python Regular Expressions][11] is a step-by-step simplified guide covering several RegEx aspects that are specific to Python.


## Riddles

Riddles are a great way to learn and practice RegEx. Check the following riddles for yourself.

### RegEx Crossword Puzzles

When it comes to RegEx riddles, [regexcrossword][7] offers an interesting approach of combining RegEx with the traditional crossword puzzles. They are classified according to difficulty level.

### BBC Radio 4 - RegEx Crossword Puzzle

BBC Radio 4 with their "Puzzle for Today" also offered a [BBC Radio 4 - RegEx crossword puzzle][8].

### Software Engineering Handbook - RegEx Crossword Puzzle

Here we also offer a [Handbook RegEx crossword puzzle][9] with a [detailed solution][10].

---

[1]: https://en.wikipedia.org/wiki/Regular_expression
[2]: https://dzone.com/articles/abc-of-regex
[3]: http://www.rexegg.com/regex-quickstart.html
[4]: https://regex101.com/
[5]: https://regexr.com/
[6]: https://www.regextester.com/
[7]: https://regexcrossword.com/challenges
[8]: https://www.bbc.co.uk/programmes/articles/5LCB3rN2dWLqsmGMy5KYtBf/puzzle-for-today
[9]: ./RegEx%20Crossword%20Puzzle%20-%20Problem%20with%20Example.md
[10]: ./RegEx%20Crossword%20Puzzle%20-%20Solution.md
[11]: https://www.machinelearningplus.com/python/python-regex-tutorial-examples/
