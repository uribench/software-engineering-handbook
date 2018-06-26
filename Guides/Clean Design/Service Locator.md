# Service Locator

[James Kovacs][1] addresses the need for service locator as a mean for achieving decoupling 
high-level and lower-level components:

> Although the concrete implementations only depend on an interface, the question remains how the 
> concrete classes "find" each other.
> 
> One solution is to use a factory for creating concrete classes’ instances. This provides a central 
> place to switch to concrete classes by simply changing the factory method. Another name for this 
> technique is service location, and the factory class responsible for managing instances is called 
> a service locator.
> 
> The functionality within the ServiceLocator could be based on data read from a configuration file 
> or database, or it could be directly wired up with code. In either case, you now have centralized 
> object creation for your dependencies.
> 
> Unit testing of isolated components can be accomplished by configuring the service locator with 
> fake or mock objects rather than the real implementations.
> 
> Service location has a few disadvantages, however. First, dependencies are hidden in the 
> higher-level class. You cannot tell that high-level module depends on low-level modules from its 
> public signature—only by examining its code. If you need to supply different concrete types for 
> the same interface, you must resort to overloaded Find methods. This requires you to make 
> decisions about whether an alternate type is required when you're implementing the factory class. 
> For example, you can't reconfigure the ServiceLocator to substitute a low-level module at 
> deployment time for specific requests. But even with these disadvantages, service location is easy 
> to understand and better than hardcoding your dependencies.


---

**Related Guides:**

- [Clean Design Principles][2]
- [Clean Design Objectives][3]
- [Layering an Application][4]
- [Dependency Inversion Principle][5]

---

[1]: http://download.microsoft.com/download/3/A/7/3A7FA450-1F33-41F7-9E6D-3AA95B5A6AEA/MSDNMagazineMarch2008en-us.chm
[2]: /Guides/Clean%20Design/Clean%20Design%20Principles
[3]: /Guides/Clean%20Design/Clean%20Design%20Objectives
[4]: /Guides/Clean%20Design/Layering%20an%20Application
[5]: /Guides/Clean%20Design/Dependency%20Inversion%20Principle
