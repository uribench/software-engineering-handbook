# Clean Design Principles

Fact is that in Software Engineering, requirements change, technologies change, developers change, 
and the business changes. As stated by [James Kovacs][1] in [Tame Your Software Dependencies for 
More Flexible Apps][2]: "Practically the only constant in this industry is change."

The main design question becomes: How is your design going to respond to those changes?

James Kovacs suggests the following answer to the above question: "By creating loosely coupled 
designs, software can better respond to inevitable, and many times unforeseeable, changes."

It seems that from all the common traits of a clear design, the main attribute is loose coupling.
Layering could be one way to achieve decoupling. However, keep in mind that layering an application 
does not guarantee loose coupling!

So, if layering is not enough, how loose coupling can be achieved?

The following related guides elaborate on loose coupling and provide different perspectives on the 
subject. Several relevant design patterns are also presented. 

---

**Related Guides:**

- [Clean Design Objectives][3]
- [Layering an Application][4]
- [Dependency Inversion Principle][5]
- [Service Locator][6]

---

[1]: http://jameskovacs.com/2008/03/13/loosen-up-tame-your-software-dependencies-for-more-flexible-apps/
[2]: http://download.microsoft.com/download/3/A/7/3A7FA450-1F33-41F7-9E6D-3AA95B5A6AEA/MSDNMagazineMarch2008en-us.chm
[3]: /Guides/Clean%20Design/Clean%20Design%20Objectives
[4]: /Guides/Clean%20Design/Layering%20an%20Application
[5]: /Guides/Clean%20Design/Dependency%20Inversion%20Principle
[6]: /Guides/Clean%20Design/Service%20Locator
