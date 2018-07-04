# Simple Workflow for Contributing to the Handbook

The following workflow describes the minimal steps required to contribute content for a new 
subject: 

1. [Select Subject](#select-subject)
2. [Create Content](#create-content)
3. [Submit Pull Request](#submit-pull-request)

## Select Subject

Think about a subject that is of interest to Software Engineers and from your own experience is not
covered well by existing tutorials or is not easily accessible.

Explore the [detailed Table of Contents (TOC)](toc.md) to get ideas of such subjects and identify 
where your contribution may fit. If you think that the current TOC requires changes, we recommend 
that you open an issue that presents your change or fix.

## Create Content

Goto the [handbook repository on GitHub][1] and use the 'Create new file' button to start editing 
the content online. When finished, optionally add description using the 'Propose new file' dialog, 
and finally submit the file using the 'Propose new file' button.

Note: Since you are creating a file in a project you don’t have write access to. Submitting a 
change will create the file in a new branch in your fork, so you can send a pull request. Visit 
[Contributing to an Open Source Project][4] for more details on fork and pull request.

### Prerequisites

Learn about the differences between [Guides](Guides) and [Topics](Topics) in the context of the 
Software Engineering Handbook.

### Guides and Topics Authoring

Create Guides and/or Topics for the selected subject as described above. Include appropriate 
references to external sources with minimal duplications of exiting materials. Create internal 
links associating between the Guides and Topics documents for the subject. 

### Content Style Guides

* Use [Markdown][2].
* See relevant examples in [Guides](Guides) and [Topics](Topics) directories.
* Use preview tools for Markdown (e.g., GitHub itself for files ending with `.md`).

## Submit Pull Request

We use [GitHub Flow][3], which means all changes happen through [pull requests][4].

If you are a first time contributor, we recommend that you open an issue that presents your 
change or fix, before submitting a pull request.

---

[1]: https://github.com/uribench/software-engineering-handbook
[2]: https://daringfireball.net/projects/markdown
[3]: https://guides.github.com/introduction/flow/index.html
[4]: http://software-engineering-handbook.com/Guides/Git/Contributing%20to%20an%20Open%20Source%20Project
