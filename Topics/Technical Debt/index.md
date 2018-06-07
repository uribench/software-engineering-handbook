# Technical Debt

A practical definition of technical debt *could* be...

**Technical debt is a measure of cost-of-change and risk-of-defects**

There are many types of debt but a basic example will help to illustrate the above...

Imagine a function with...
- 1000+ lines of code
- Multiple levels of nested indentation
- Many local and non-local variables
- No automated unit test coverage

If you care about software engineering, you can probably already feel a chill running down your spine!

This is because you intuitively know that such a function is going to be painful to understand and change.

The cost-of-change is high because it is time-consuming to...
- Read and understand the function
- Identify the place(s) to make changes
- Predict side-effects on control flow
- Predict side-effects on shared state
- Manually regression test all paths

The risk-of-defects is high because there are...
- Unpredictable side-effects on control flow
- Unpredictable side-effects on shared state
- No regression protection from automated tests
- Many hard to identify paths making good tests hard to define

The above is a simple example of some dirty code. Debt comes in many other forms.

You have debt if there are characteristics of your architecture, design, codebase, build & deployment, documentation, etc., that make change expensive and defects likely.

It is not always easy to identify how the axes of change might evolve in your product.

It is a risky bet for developers to write speculative code based on guesses about these axes.

Practicing clean code is a good preparation for dealing with debt. It is also a reduction in debt in itself. 

Without clean code, it is tough to refactor as the axes of change of your system become clearer.

>Dirty code is to technical debt as the pawn broker is to financial debt. 
>Don't think you are ever going to get your code back.
*[Ward Cunningham, 2009, Twitter](http://twitter.com/WardCunningham/status/3742903303)* 
