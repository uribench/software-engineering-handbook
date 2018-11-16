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
get better or worse?

Each hotspot is also assigned a [Code Biomarker Score][4]. In medicine, a biomarker is a measure that might indicate a
particular disease or physiological state of an organism. CodeScene’s biomarkers do the same for code, and each
hotspots is scored from `A` to `E` where `A` is the best and `E` indicates code with severe maintenance problems.

The next figure shows an example on a prioritized hotspot in the Android codebase with a biomarker score of `E`:

![CodeScene](/images/codescene-android.png)

The hotspot analysis is completely automated, and CodeScene is able to prioritize a small part of your codebase –
typically 2-4% – that identifies the most likely return on any code quality investments. Let's see how to act on it.

### Drill Deeper With Virtual Code Reviews and X-Ray



## Look Beyond Code to Uncover the Social Side of Technical Debt

## Supported Platforms and Programming Languages

CodeScene works with Git repositories out of the box. In case you have another version-control system you have to convert
to a (read-only) Git repository for the analysis. This is an [automated conversion][4]. Continue to work in your
version-control of choice, and synchronize changes to the read-only Git repository under analysis.

CodeScene supports all major programming languages, and there's a complete list of supported languages
in [CodeScene's documentation][4].


---

[1]: https://empear.com/
[2]: https://empear.com/blog/code-biomarkers/
[3]: https://git-scm.com/book/en/v2/Git-and-Other-Systems-Migrating-to-Git
[4]: https://docs.enterprise.codescene.io/versions/2.7.0/guides/technical/xray.html