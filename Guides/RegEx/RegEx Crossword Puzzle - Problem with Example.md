# Can you solve this RegEx Crossword Puzzle?

## Example - RegEx "Hello World" Crossword Puzzle

![RegEx "Hello World" example][1]

![Very basic RegEx cheat sheet][2]

## Problem - RegEx Crossword Puzzle

![Problem Image][3]

## How to Play

Regex Crossword is a game similar to the traditional crossword puzzle, where you must guess the correct letters in the horizontal and vertical lines of a grid. In Regex Crossword you are given rows and columns regular expression patterns that tell you which letters are allowed. To complete the puzzle, find the letter
matching both the horizontal and vertical RegEx for each square. The direction for rows is from left to right and for columns is from top to bottom.

\*Inspired by [RegEx Crossword][4].

## Hints

Need help? Use the following hints:

* **Practice**: Go to [RegEx Crossword][4] to practice RegEx Crosswords at various levels, then come back and try to solve this puzzle.
* **Walkthrough**: Visit [RegEx101][5] to experiment with RegEx and get explanations for specific patterns that are challenging you in this puzzle. Copy the pattern you are interested in from the following list and paste it on RegEx101. The results of the analysis done by RegEx101 can be seen on the **EXPLANATION** panel.

**Rows Patterns:**

[^CDAQ][abcdeo\s]\*

(s|t)(emp|map)\1s\s\1

(he|it).[em]\*(.)\2\s

t(.)[gr\s]\*\1[^abc].

**Columns Patterns:**

(A|B)[th]\*

\[a-c](.)\1o

[d-m]\*(?=\s)[\s]\*

\s[l-r]\*g

(er|ct)\*

(o)(.)\2\1

(sw|d\s)\*

(\s|et)\*!

## Solution

To the [solution][6].

---

[1]: ./images/Hello%20World%20Puzzle%20Example.jpg
[2]: ./images/Very%20Basic%20RegEx%20Cheat%20Sheet.jpg
[3]: ./images/RegEx%20Crossword%20Puzzle%20-%20Problem%20without%20Hints.jpg
[4]: https://regexcrossword.com/
[5]: https://regex101.com/
[6]: ./RegEx%20Crossword%20Puzzle%20-%20Solution.md