# Technical Debt Overview

[Technical Debt][1] is a metaphor developed by [Ward Cunningham][2] to help dealing effectively with 
code design problems. It compares taking bad design choices to taking a financial debt. The interest 
on the debt has to be continually payed, as long as the principle is not payed down by refactoring 
the code into a better design. 

Technical debt is inevitable and thus should be expected. It has multiple forms and causes, some are 
intentional, meant to exploit a market opportunity, and some are unintentional, due to lack of 
knowledge or short-sightedness.

Beyond a certain level of debt the code decays to the point in which making changes is becoming 
expensive and the risk of defects increases. Therefore, a decision of continuing paying the interest 
versus paying down the principal, and thus reduce interest payments in the future, has to be taken 
continuously.

In order to manage Technical Debt effectively, the following questions have to be addressed:

- What are the causes and effects of Technical Debt?
- How to prevent unintentional Technical Debt?
- How to measure and monetize Technical Debt before and after it has been created?
- How to plan for Technical Debt repayment?

The following practical guides attempt to address some of these questions:

- [Basic Example of Function Level Technical Debt][3]

---

[1]: https://en.wikipedia.org/wiki/Technical_debt
[2]: https://en.wikipedia.org/wiki/Ward_Cunningham
[3]: /Topics/Technical%20Debt