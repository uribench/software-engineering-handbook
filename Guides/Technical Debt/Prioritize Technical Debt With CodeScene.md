# Prioritize Technical Debt with CodeScene

[CodeScene][1] is a behavioral code analysis tool that identifies and prioritizes technical debt. The main difference
between CodeScene’s behavioral code analysis and traditional code scanning techniques is that static analysis works on
a snapshot of the codebase while CodeScene considers the temporal dimension and evolution of the whole system. This
makes it possible for CodeScene to prioritize technical debt and code quality issues based on how the organization
actually works with the code. Hence, behavioral code analysis limits the results to information that is relevant,
actionable, and translates into business value.

CodeScene works by analysing behavioral data as recorded in version-control systems and, optionally, project management tools:

![CodeScene](/images/codescene-how.png)


## Know your Hotspots

A hotspot is complicated code that the organization has to work with often. CodeScene identifies hotspots by measuring
how the developers interact with the codebase, and we detect in which direction each piece of code evolves – does it
get better or worse? In principle, the change frequency of each hotspot is used as a proxy for the *interest rate* on
any technical debt we might find in that code.

To identify potential problems, each hotspot is assigned a [Code Biomarker Score][4]. In medicine, a biomarker is a
measure that might indicate a particular disease or physiological state of an organism. CodeScene’s biomarkers do the
same for code, and each hotspots is scored from `A` to `E` where `A` is the best and `E` indicates code with severe
maintenance problems.

The next figure shows an example on how CodeScene visualizes a prioritized hotspot in the Android codebase with
a biomarker score of `E`:

![CodeScene](/images/codescene-android.png)

The hotspot analysis is completely automated, and CodeScene is able to prioritize a small part of your codebase –
typically 2-4% – that identifies the most likely return on any code quality investments. Let's see how to act on it.

### Drill Deeper With Virtual Code Reviews

Once you have identified a prioritized hotspot, you request a virtual code review to get a detailed description of
the potential quality issues in that module. The virtual code review will aggregate the most significant
metrics for your chosen file:

![CodeScene's Virtual Code Reviewer](/images/codescene-virtual-code-reviewer.png)

The virtual code reviewer combines the social and technical analysis data you need to assess the severity of the
hotspot:

* Review the detailed biomarker indications to spot maintenance and quality issues.
* Detect potential inter-team coordination bottlenecks that should drive refactorings through the social metrics such as the team autonomy measure.
* See if it's a growing problem in the Complexity Trend.
* Investigate the change coupling, filtered for your selected file under review.
* Use the defect trend to estimate the cost of any technical or social debt you might find in the review.

### Prioritize Small and Iterative Refactorings with the X-Ray Analysis

Based on the outcome of our review we might detect the need to initiate some refactorings to pay-off the accumulated debt.
This might easily turn into a Sisyphus task due to the severity and scale of the identified hotspot. For example, the
hotspot identified in Android (see the previous figure) is a file with +20.000 lines of code! Where do we start?

In addition, the virtual code review might warn us that there's a high degree of development fragmentation with much
parallel work by different teams in the identified hotspot. That means we need to keep our refactoring efforts small
and iterative.

CodeScene's X-Ray analysis lets you identify hotspots on a function/method level. That means you can use the X-Ray
results to drive refactorings. Let's look at an example from our Android hotspot:

![An X-Ray Analysis of a Large Hotspot](/images/codescene-xray.png)

In the preceding X-Ray visualization, we see that the number one hotspot on a method level is `handleMessage` with
500 lines of code that changes often and has a complexity number, `106`, that is well above the cut-off point for
"very high complexity", which is `15`. The high change frequency, `98` changes to this method alone, indicates that
any improvements we can do to that code are likely to give an immediate return on investment.

Now, a method with 500 lines of code is a lot. But it's still less than 20.000 lines, which was the size of the
hotspot. And it's definitely less than 3 million lines of code, which is the size of the total Android codebase. More
important, we are now on a level where we can do a focused refactoring based on data from how we -- as an organization --
actually works with the code. Use this information to your advantage.

## Supported Platforms and Programming Languages

CodeScene works with Git repositories out of the box. In case you have another version-control system you have to convert
to a (read-only) Git repository for the analysis. This is an [automated conversion][3]. Continue to work in your
version-control of choice, and synchronize changes to the read-only Git repository under analysis.

CodeScene supports all major programming languages, and there's a complete list of supported languages
in [CodeScene's documentation][4].

---

[1]: https://empear.com/
[2]: https://empear.com/blog/code-biomarkers/
[3]: https://git-scm.com/book/en/v2/Git-and-Other-Systems-Migrating-to-Git
[4]: https://docs.enterprise.codescene.io/versions/2.7.0/guides/technical/xray.html