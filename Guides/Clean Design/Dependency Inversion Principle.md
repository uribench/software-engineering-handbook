# Dependency Inversion Principle

In "programming to contract" technique you can decouple your higher-level component from its 
lower-level dependencies by interacting with your dependencies via interfaces rather than their 
concrete classes. 

This simple change to using interfaces (or an abstract base class) means that you can substitute an 
alternate implementation for any of the dependencies. This also means that you can [substitute fakes 
or mocks during testing][1].

This principle for decoupling high-level and lower-level components is called the **Dependency 
Inversion Principle** (DIP). 

Robert C. Martin defines in [Clean Code - A Handbook of Agile Software Craftsmanship][2] the 
following relations:

**Dependency Injection** (DI) is the application of DIP and **Inversion of Control** (IoC) to 
dependency management.

As Robert C. Martin says in [Agile Software Development, Principles, Patterns, and 
Practices][3]: "High-level modules should not depend on low-level modules. Both should depend on 
abstractions."

One of the [seminal papers on Dependency Injection][4] is by Martin Fowler. In this paper Fowler 
describes three types of Dependency Injection implementations:

- Constructor Injection
- Setter Injection
- Interface Injection

---

**Related Guides:**

- [Clean Design Principles][5]
- [Clean Design Objectives][6]
- [Layering an Application][7]
- [Service Locator][8]

---

[1]: http://download.microsoft.com/download/3/A/7/3A7FA450-1F33-41F7-9E6D-3AA95B5A6AEA/MSDNMagazineMarch2008en-us.chm
[2]: https://www.goodreads.com/book/show/3735293-clean-code
[3]: https://www.goodreads.com/book/show/84985.Agile_Software_Development_Principles_Patterns_and_Practices
[4]: http://martinfowler.com/articles/injection.html 
[5]: /Guides/Clean%20Design/Clean%20Design%20Principles
[6]: /Guides/Clean%20Design/Clean%20Design%20Objectives
[7]: /Guides/Clean%20Design/Layering%20an%20Application
[8]: /Guides/Clean%20Design/Service%20Locator
