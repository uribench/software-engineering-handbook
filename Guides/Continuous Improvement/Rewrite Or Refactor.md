# Rewrite or Refactor
The software rewrite vs refactor debate  
![Debate](/images/2012-wildebeest-fight.jpg "(c) Yathin sk on Wikimedia")

## When is "Rewrite" an option?
Recently I read the book ["Knigge für Softwarearchitekten"][1] (translates to something like 'etiquette manual for software architects') from two well-known German authors of software engineering textbooks.  
One topic within this book addresses the "Rewrite or Refactor" question: When is it feasible to "rewrite" a complete (working) product from scratch?  
The (working) product is the software that produces the current value for the organization and hence needs to be maintained. Sometimes people talk lightly of this product as "legacy software" and think it needs a rewrite to cope with new technologies or requirements.  

But what does "legacy software" mean?  
I personally like a definition from Michael Feathers: "legacy code is code without tests" (author of ["Working Effectively with Legacy Code"][2]).  
As a consequence, the current product, is not legacy software as long as it has tests. And therefore new source code, just written some days ago is legacy, if it has no tests. As discussed further on this article, the current product is the place where all the business value is currently implemented. It can be seen as the business treasure chamber.  
Often there is the assumption that "exiting new things" cannot be integrated into old software. I think quite the opposite is true; with tests in place (and/or a good modularized architecture), it is possible to do refactorings to address also fairly major architectural changes without throwing away the code.  

The authors of the book are not discussing about small services (e.g. micro services) or tools within one product, where rewriting may be the right option, but instead refer to complete re-architecting and rewriting a complex software product.  
They reference the well-known article ["Things You Should Never Do, Part I"][3] from Joel Spolsky. In his article, Joel also argues against rewrite and mentions Netscape as a negative example. They went out of business because they decided to rewrite the browser engine from scratch. While this took years to finish, they neglected their working product. 

![OldvsModern](/images/Old_tower_with_modern_building.jpg "(c) Piotrus on Wikimedia")

## A small research on the web
From this starting point, I tried to do some web research on this topic.
I found a nice article from Robert C. Martin ["The Big Redesign In The Sky"][4] with the following statement:

> When is a redesign the right strategy?  
> I'm glad you asked that question.  
> Here's the answer: Never!

It is a nice read and Uncle Bob is suggesting not to start from scratch but to continuously improve your code.  
The following article highlights the "experiences" of a software developer, gone through several rewrite attempts ["If You Must Rewrite"][5].  
This is the list of events that often happened during these rewrites:
* The rewrite took much longer than expected, during which time the business stood still while the market moved on.
* Functionality written over several years had to be re-implemented in a fraction of the time.
* The development team was immediately pressured to **get it done**. This created a sense of always being behind schedule.
* The business became frustrated and could not understand why it was taking so long.
* The rewrite provided little or no new functionality to the business.
* There were hidden business rules that had been long forgotten and no one knew what they meant.
* The old system could not be turned off until all the features were migrated to the new system.

The above experiences probably sound familiar to someone who participated in a big rewrite project.
Another article that strongly votes against rewrite and which discusses some alternatives, like evolving system / software architecture and refactoring, is ["The Big Rewrite"][6]

Even though there are alternatives to evolve an existing code base / product, the rewrite approach is often tried. The rewrite seems attractive because the team moves fast at the beginning.  
But sooner or later teams end up in the same situation: the new product has the same problems that the old product had.

The article ["Rewrites vs. refactoring: 17 essential reads for developers"][7] also collects some material around this topic.  
It refers to the book [Code Simplicity][8], by Max Kanat-Alexander, where the following checklist is shown, that claims you shall only consider a rewrite if **all** of the following are **true**:
* You've done extensive research and you're nearly certain it will be less expensive and less time-consuming to rewrite. 
* You have a ton of time to devote to building the new system.
* You're a better designer than the system's original architect. If you are the system's original architect, are you sure you're significantly better now?
* You've got a plan to get feedback from users early and often as you rewrite.
* You're rich enough and have enough time to maintain both systems while you build the new one.

## How a rewrite feels like
The article ["How to Survive a Software Rewrite"][9] comes up with a stage model that might sound familiar for some of us.  
It describes the vicious circle that often happens during rewrite projects that get under time pressure.

The possible effects of a rewrite to the competitiveness of a product is graphically illustrated within the article ["Why You Should (Almost) Never Rewrite Code - A Graphical Guide"][10]

![Competitiveness](/images/chart11.jpg "(c) VibratingMelon")

The purple graph represents the "Status Quo" of continuous development. The green graph is showing the rewrite scenario. The red line is the resulting competitiveness of the product (over time) of the rewrite.

As discussed by [Erik Dietrich][11], the author of NDepend (a static code analsysis tool for .Net), at the end it comes down to a business case, where the rewrite is almost always loosing against the refactoring approach.  
Two examples from the last years are a rewrite attempt of a big German supermarket discounter: ["Elwis" is dead: Lidl stops million-dollar project with SAP][12]

> "In the cost-benefit analysis everything speaks in favor of the further development of the Wawi (the existing product)", said the board of management after the rewrite project was stopped.

and in 2015 the logistics company DHL (from the German Post) failed when developing their [New Forwarding Environment (NFE)][13], leading to bad business results. 

> "At the same time, management is looking for other ways to create a total solution from existing systems.  
> Evolution instead of revolution"

## What does that mean for us?
It seems to be collective wisdom that a complete rewrite of a "working" software product should only be done under extreme circumstances and that an evolution of the existing product is usually the better approach.

But Lidl and DHL are not the only ones who made bad experiences.  
Also Philips had stopped a big rewrite project around the year 2000. As a consequence it was decided to pick up the existing product software from before rewrite and since then it evolved to a successful, maintainable and extensible software platform with regular releases for different diagnostic X-ray modalities.  
The continuous improvement resulted in an architecture that allows the refactoring or even exchange of certain services where necessary, to extend the platform when needed and to evolve existing ("legacy") components.  
It also led to a high quality of the developed software, recognized by e.g. winning the [TIOBE Software Quality Award][14].

## How about sustainability?
The material that I found on the web seems to clearly argue against rewrite (all opinions and experiences, not scientific evidence).  
Even though the web argues for evolution and refactoring, there are still often projects started to attempt a complete rewrite and fail.  

Can we extract best practices from these experiences?  
A good starting point could be the collection of patterns and best practices on architecture improvement, evolution and refactoring which can found at [aim42][15].  
[aim42][15] is the systematic approach to improve software systems and architectures.    
Complementing this with the test design and refactoring techniques from e.g. ["Working Effectively with Legacy Code"][2] is enabling the continuous improvement of existing software systems.


[1]: https://www.amazon.de/dp/B008XXPVFU/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1
[2]: https://www.amazon.com/Working-Effectively-Legacy-Michael-Feathers/dp/0131177052/ref=sr_1_1?ie=UTF8&qid=1542705242&sr=8-1&keywords=michael+feathers
[3]: https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/
[4]: http://www.luckymethod.com/2013/03/the-big-redesign-in-the-sky/
[5]: https://timross.wordpress.com/2010/03/15/if-you-must-rewrite/
[6]: https://jvaneyck.wordpress.com/2015/03/12/the-big-rewrite/
[7]: https://techbeacon.com/17-opinions-resources-rewrites-vs-refactoring
[8]: http://shop.oreilly.com/product/0636920022251.do
[9]: https://www.jamesshore.com/Blog/How-to-Survive-a-Rewrite.html
[10]: https://vibratingmelon.com/2011/06/10/why-you-should-almost-never-rewrite-code-a-graphical-guide/
[11]: https://blog.ndepend.com/rewrite-or-refactor/
[12]: https://www.heise.de/newsticker/meldung/Elwis-ist-tot-Lidl-stoppt-millionenschweres-Projekt-mit-SAP-4111245.html
[13]: https://www.heise.de/newsticker/meldung/Deutsche-Post-in-der-Klemme-Fehlerhafte-IT-und-globales-Frachtgeschaeft-verderben-Prognose-2866205.html
[14]: https://www.tiobe.com/tqi/awards/
[15]: https://www.aim42.org/
