# Property Based Testing

## Overview
Property Based Testing (PBT) is a way of writing unit tests that views test coverage from a different perspective; in PBT coverage is measured in terms of the input's potential values _(functional domain)_:

Typically you would write unit tests to cover how your code branches (as in flowcharts or like compound nodes of a lisp S-Expression). You think about which methods get run, and which expressions within our IF conditions, or switch statements get evaluated. PBT see coverage, instead, in terms of the possible input and output values for a function (its domain, and co-domain or range).

From the perspective of PBT coverage is the subset of all possible input values used to verify their output: If in one typical unit test one input value is put under scrutiny, then, in PBT an intelligent sampling of all possible inputs is pushed through the functions in order to confirm the test writers suppositions about the functions.

In this sense PBT is a form of _contract based programming_.

## Objectives and Scope

This guide is not an introduction into property based testing, or a tutorial on how to use a specific PBT library. Instead, it is an overview and comparison to traditional unit testing useful for developers planning to investigate the subject further.

## Development Flow

When implementing PBT, it is possible to follow Test Driven Development (TDD) and write your properties (laws) first, followed by your generators, and finally your production modules (classes) with the implemented algorithm.

## Components of PBT

### Laws
Property based testing is especially useful when you can express requirements in the form of contracts, pre, and post conditions or equivalently Laws that hold for the code under test.

An example of this type of property could be:

`Person#age(int year, int month, int day)` increases by one per increase of year by one.

Of course finding laws to fit your specific types is different than knowing what to expect for a specific value, they are related (from enough examples you can write a law, and from laws you can fill out examples).

### Generators

Generators are the mechanism through which the sample input for your tests is collected. All PBT libraries come with a set of built in generators and a mechanism to compose them as well as create your own. Through generators you are able to write up the pre-conditions to your properties.

### Shrinking

Shrinking is an optional feature of some property based testing libraries. Because generators are used to generate a lot of different sample input values, it can be difficult to isolate the root cause of failures. i.e. identifying why it failed for: 101, 107, and 73. Shrinking is then the library's attempt to find the "smallest" example for which the defined property is disproved. Different libraries have different mechanisms to automate this process of narrowing the failure inputs, and when this feature works well, it is extremely useful.

### Stateful Properties

Some code is better expressed by state machines or message passing objects, that respond differently to the same input. When you want to extend your pre and post conditions to some additional state outside the function you will want your library to support a way to specify these additional restrictions. Most decent libraries offer a way to extend pre conditions as the tuple (state, sample) => (new state, result)

### Concurrent Properties

Some code is expected to be invariant in the presence of non-deterministic execution. To this end some libraries are able to confirm properties hold across distributed systems.

## Benefits and Drawbacks over Traditional Unit Testing

By exchanging hand picked inputs in favor of multiple random samples property based testing:

* PBT can find errors even after coverage is at 100%.
* PBTs are generally slower to run than similar unit tests.
* PBT allows you to think in terms of _pre_ and _post_ conditions.
* PBT reduces the appearance of magic literals in your test code.
* PBT reduces code duplication by distinguishing between properties and
  generators.

## References

- [What-If - We use property based testing when doing our unit tests][1]
  - [What-If source][2]
- [John Hughes - Testing the hard stuff and staying sane][3]
- [Testing, done right How to make your code bulletproof with property testing][4]
- [My Take on Property-Based Testing - Brujo Benavides][5]
- [Foundations of Property-Based Testing][6]
- [QuickCheck Wikipedia Article][7]

### Libraries

The [QuickCheck][7] Wikipedia article has several implementations for a wider variety of languages. Here is a brief selection of a PBT library for three popular languages:

- [JSVerify (javascript)][8]
- [JUnit-quickcheck (java)][9]
- [Hypothesis (python)][10]

---

[1]: https://www.youtube.com/playlist?list=PLGlHOtaEF8ytlwlksmhWAtnERXmo40pAN
[2]: https://github.com/software-practices/whatifs
[3]: https://www.youtube.com/watch?v=zi0rHwfiX1Q
[4]: https://techbeacon.com/app-dev-testing/how-make-your-code-bulletproof-property-testing
[5]: https://medium.com/erlang-battleground/property-based-testing-erlang-elixir-de72ad24966b
[6]: https://propertesting.com/book_foundations_of_property_based_testing.html
[7]: https://en.wikipedia.org/wiki/QuickCheck
[8]: https://jsverify.github.io/
[9]: https://github.com/pholser/junit-quickcheck/
[10]: https://hypothesis.works/
