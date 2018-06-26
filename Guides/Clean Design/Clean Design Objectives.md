# Clean Design Objectives

One of the ways to focus on the objectives of a clean design is by understanding what bad design is. 
Robert C. Martin describes bad design in [Agile Software Development, Principles, Patterns, and 
Practices][1] as follows: 

A piece of software that fulfills its requirements and yet exhibits any or all of the following 
three traits has a bad design:

1.  It is hard to change because every change affects too many other parts of the system. (Rigidity)
2.  When you make a change, unexpected parts of the system break. (Fragility)
3.  It is hard to reuse in another application because it cannot be disentangled from the current 
    application. (Immobility)

What is it that makes a design rigid, fragile and immobile? 

It is the **interdependence** of the modules within that design.

Good design, according to [James Kovacs][3], is about **reversibility**. How easily can you change 
your mind with respect to design decisions? Do you have an application architecture that responds 
well to change? How this goal can be achieved without unnecessarily making too complex design. 

The intent is not to build an infinitely extensible but hugely complex and unusable generic framework.

Note: Robert C. Martin has a [follow up book][2] presenting a series of case studies illustrating 
the fundamentals of Agile development and Agile design, and how to move from UML models to real C# 
code.

---

**Related Guides:**

- [Clean Design Principles][4]
- [Layering an Application][5]
- [Dependency Inversion Principle][6]
- [Service Locator][7]

---

[1]: https://www.goodreads.com/book/show/84985.Agile_Software_Development_Principles_Patterns_and_Practices
[2]: http://druss.co/wp-content/uploads/2013/10/Agile-Principles-Patterns-and-Practices-in-C.pdf
[3]: http://download.microsoft.com/download/3/A/7/3A7FA450-1F33-41F7-9E6D-3AA95B5A6AEA/MSDNMagazineMarch2008en-us.chm
[4]: /Guides/Clean%20Design/Clean%20Design%20Principles
[5]: /Guides/Clean%20Design/Layering%20an%20Application
[6]: /Guides/Clean%20Design/Dependency%20Inversion%20Principle
[7]: /Guides/Clean%20Design/Service%20Locator
