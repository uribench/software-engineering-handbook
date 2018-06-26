# Layering an Application

[James Kovacs][1] examines in [Tame Your Software Dependencies for More Flexible Apps][2] 
application design that relies on layering. Layers as coherent clusters of responsibility are a good 
design technique. 

It is very common to have layers being aware only of the layer beneath them. However, direct 
coupling of upper layers to lower layers, increases coupling and makes the application difficult to 
test. 

Why is James Kovacs concerned with testability? Because testability is a good barometer of coupling. 
If you can't easily instantiate a class in a test, you have a coupling problem.

One conclusion from the above is: **Layering an application does not guarantee loose coupling!**

---

**Related Guides:**

- [Clean Design Principles][3]
- [Clean Design Objectives][4]
- [Dependency Inversion Principle][5]
- [Service Locator][6]

---

[1]: http://jameskovacs.com/2008/03/13/loosen-up-tame-your-software-dependencies-for-more-flexible-apps/
[2]: http://download.microsoft.com/download/3/A/7/3A7FA450-1F33-41F7-9E6D-3AA95B5A6AEA/MSDNMagazineMarch2008en-us.chm
[3]: /Guides/Clean%20Design/Clean%20Design%20Principles
[4]: /Guides/Clean%20Design/Clean%20Design%20Objectives
[5]: /Guides/Clean%20Design/Dependency%20Inversion%20Principle
[6]: /Guides/Clean%20Design/Service%20Locator
