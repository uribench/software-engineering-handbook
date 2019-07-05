# Property Based Testing Overview
Property based testing is a way of writing unit tests that views test coverage 
from a different perspective.

Typically you would write unit tests to cover how your code branches (very much 
like branches within a lisp S-expression). You think about which methods get run,
and which branches within our IF conditions, or switch statements get executed. 
Property based tests see coverage instead in terms of the possible input and 
output values for a function (its domain, and co-domain or range). From the 
perspective of property based tests coverage is the subset of all possible input
values used to verify their output: If in one typical unit test one input value 
is put under scrutiny, then, in property based testing an intelligent sampling 
of inputs is pushed through the functions in order to confirm the test writers 
suppositions about the functions.

In this sense Property based tests are a form of contract based programming. 

# Laws
Property based testing is especially useful when you can express requirements in
the form of contracts, pre, and post conditions or equivalently Laws that hold 
for the code under test.

An example of this type of property could be:

`Person#age(int year, int month, int day)` increases by one per increase of year
by one.

Of course finding laws to fit your specific types is different than knowing what
to expect for a specific value, they are of course related (from enough examples
you can write a law, and from laws you can fill out examples).

# Generators

Generators are the mechanism through which the sample input for your tests is 
collected. All property based testing libraries come with a set if built in 
generators and a mechanism to compose them as well as create your own. Through 
generators you are able to write up the pre-conditions to your properties.

# Shrinking

Shrinking is an optional feature of some property based testing libraries. 
Because generators are used to generate a lot of different sample input values, 
it can be difficult to isolate the root cause of failures. i.e. identifying why 
it failed for: 101, 107, and 73. Shrinking is then the library's attempt to find
the "smallest" example for which the defined property is disproved. Different 
libraries have different mechanisms to automate this process of narrowing the 
failure inputs, and when this feature works well, it is terribly useful. 

# Stateful Properties

Some code is better expressed by state machines or message passing objects, that
respond differently to the same input. When you want to extend your pre and post
conditions to some additional state outside the function you will want your 
library to support a way to specify these additional restrictions. Most decent 
libraries offer a way to extend pre conditions as the tuple (state, sample) => 
(new state, result)

# Libraries

Here is a non-exhaustive list of libraries selected by language

- [QuickCheck](https://github.com/nick8325/quickcheck) (_original_ Haskell library)
- [ScalaCheck](https://www.scalacheck.org/) (scala)
- [RapidCheck](https://github.com/emil-e/rapidcheck) (c++)
- [FSCheck](https://fscheck.github.io/FsCheck/) (c# and .net)
- [JSVerify (javascript)](https://jsverify.github.io/)

# References

- [What-If - We use property based testing when doing our unit tests.](https://www.youtube.com/playlist?list=PLGlHOtaEF8ytlwlksmhWAtnERXmo40pAN)
  - [source](https://github.com/software-practices/whatifs)
- [John Hughes - Testing the hard stuff and staying sane](https://www.youtube.com/watch?v=zi0rHwfiX1Q)
- [Testing, done right How to make your code bulletproof with property testing](https://techbeacon.com/app-dev-testing/how-make-your-code-bulletproof-property-testing)
- [My Take on Property-Based Testing - Brujo Benavides](https://medium.com/erlang-battleground/property-based-testing-erlang-elixir-de72ad24966b)
- [Foundations of Property-Based Testing](https://propertesting.com/book_foundations_of_property_based_testing.html)
