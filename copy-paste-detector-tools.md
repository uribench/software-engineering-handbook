# Code Duplication Detection Tools: Comprehensive Evaluation

One of the stems in achieving code quality is to avoid duplication in the source code. Duplication in code causes the program to have more lines of unnecessary code. Over time, code changes in the duplicated parts may be done inconsistently. Hence, increasing maintenance cost and changes of having defects. 

There are no best practices in this area and practices that are proven in some contexts, may not be good for others. 

Clean code practices do not have to be an expensive or a major undertaking. It is about the ability to improve the code incrementally and achieve a significant cumulative impact on the improvement journey.

## What is Duplicate Code or Redundant Code?  

> **Duplicate Code** is a computer programming term for a sequence of source **code** that occurs more than once, either within a program or across different programs owned or maintained by the same entity. 

> Some of the ways in which two code sequences can be duplicates of each other are to be character-for-character identical, character-for-character identical with white space characters and comments being ignored, token-for-token identical, token-for-token identical with occasional variation or functionally identical.

Source: wiki

Hence, two code blocks may be considered as duplicates, even if they are not completely identical (i.e., copy/paste) but have few occasionally different tokens, or have an identical functionality. The later is more difficult to detect.

## Tool selection criteria

When it comes to cherry-pick a tool for inspecting on duplicate code/code similarity, there are scores of open source tools available in the market. Often, it is really confusing for a developer on which tool to choose, as there is no magic bullet for the same. This article wades through most commonly used tools and provides a comprehensive review on the same based on the below mentioned evaluation criteria:

* Open source software (**OPS**)
* Languages supported (**LAS**)
* Integration with CI and Fail the build (**CIF**)
* Ability to set the token limit (**TKN**)
* Reporting formats available (**RPT**)
* Available as plugin ( **PLG**)
* Documentation available (**DOC**)
* User interface available (**GUI**)
* Command line interface (**CLI**)

Additional criteria for inclusion was the tool must mainly compatible with JAVA/C/C# and also the ease of running setting up and running the tool. Paid tools are discarded

Below are some of the tools that can be used depending on your preferences:

| Tool Name                   | OPS | LAS            | CIF | TKN | RPT                | PLG  | DOC | GUI | CLI |
|:----------------------------|:---:|:--------------:|:---:|:---:|:------------------:|:----:|:---:|:---:|:---:|
| [Clone Detective for VS][2] | Yes | C, C#          | No  | No  | No                 | Yes  | (1) | Yes | No  |
| [CPD by PMD][3]             | Yes | [Link][4]      | Yes | Yes | XML, CSV, Text (2) | Yes  | Yes | Yes | Yes |
| [JSCPD][5]                  | Yes | [150+][6]      | Yes | Yes | JSON, XML, HTML    | No   | Yes | No  | Yes |
| [JSINSPECT][7] (3)          | Yes | ES6, JSX, Flow | Yes | Yes | JSON, XML          | (4)  | Yes | No  | Yes |
| [DupFinder][8]              | Yes | C#, VB.NET     | Yes | Yes | XML, HTML (5)      | Yes  | Yes | No  | Yes |
| [Simian][9]                 | Yes | Many (6)       | Yes | Yes | Text/Console       | (7)  | Yes | No  | Yes |
| [Atomiq][10]                | Yes | Many (8)       | Yes | Yes | (9)                | (10) | Yes | Yes | (9) |

Notes:

1. Clone Detective VS - Documentation are not maintained
2. PMD's CPD reporting default format is Text
3. JSINSPECT - For structurally similar JS code
4. JSINSPECT can be integrated with VSS Code
5. DupFinder (Jet brains tool) supports HTML reporting by applying XSL transformation on XML output
6. Simian supports Java, C#, C, C++, Ruby, Objective -C, Groovy, Swift
7. Simian is available as IntelliJ plugin
8. Atomiq supports C#, VB.Net, ASPX, Ruby, Python, Java, C, C++, ActionScript, and XAML
9. Atomiq console edition supports HTML and CLI
10. Atomiq is Standalone

## Conclusion

Although not everyone fits the mold, through this study there is no way to establish an efficient tool for detecting all facets of code duplication parameters. But the above table would help to choose the most appropriate tool for specific needs. In the meantime, here's a tip - JSCPD seems to be a better tool to start with; having support for 150+ programming languages and various command line options, this should fit the bill.

[1]: https://en.wikipedia.org/wiki/Duplicate_code
[2]: https://github.com/terrajobst/clonedetective-vs
[3]: https://pmd.github.io/
[4]: https://pmd.github.io/latest/pmd_userdocs_cpd.html#supported-languages
[5]: https://github.com/kucherenko/jscpd
[6]: https://github.com/kucherenko/jscpd/blob/HEAD/docs/supported_formats.md
[7]: https://github.com/danielstjules/jsinspect
[8]: https://www.jetbrains.com/help/resharper/dupFinder.html
[9]: https://www.harukizaemon.com/simian/
[10]: http://www.getatomiq.com/
