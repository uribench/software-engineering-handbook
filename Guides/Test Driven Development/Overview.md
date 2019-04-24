# Test Driven Development

Test driven development (TDD) is a way of developing software that provides the programmer with a level of confidence in their code that they have not had, or at least shouldn't have had, in the past.

Test Driven Development is a means to an end.  The end goal is to have clean code that we are not afraid to refactor when necessary, TDD can get us to this goal.  Tests offer the confidence necessary to feel free to refactor.

## The Laws of TDD

Robert C. Martin (Uncle Bob) is a large proponent of [Test Driven Development][1].  He defines three "laws" of TDD to define the cycle used while developing code.

1.  You are not allowed to write any production code unless it is to make a failing unit test pass.
2.  You are not allowed to write any more of a unit test than is sufficient to fail; and compilation failures are failures.
3.  You are not allowed to write any more production code than is sufficient to pass the one failing unit test.

Uncle Bob calls these three laws the _nano-cycle_ of TDD.  They are to be followed for _every_ line of code that you write, and executed many times during the developing of a method.

## TDD Development Iteration Steps

1.  Write a failing test
2.  Implement the production code necessary to make the test past.
3.  Refactor and remove _all_ duplication.

## Practice Makes Perfect

Test Driven Development can be difficult to master.  The best way to master something is to practice it.  TDD [_katas_][3] is one way to do this.  A kata, defined by wikipedia, is ".. an exercise in programming which helps programmers hone their skills through practice and repetition."  A list of different TDD katas can be found [here][4].  The provided [example](/Example) is one such exercise.

[1]:http://butunclebob.com/ArticleS.UncleBob.TheThreeRulesOfTdd
[2]:https://blog.cleancoder.com/uncle-bob/2014/12/17/TheCyclesOfTDD.html
[3]:https://en.wikipedia.org/wiki/Kata_(programming)
[4]:https://sites.google.com/site/tddproblems/all-problems-1
