# Typical Workflow for Contributing to the Handbook

The following workflow describes the typical steps required to contribute contents for a new 
subject: 

1. [Select a Subject](#select-a-subject)
2. [Fork the Handbook Repository](#fork-the-handbook-repository)
3. [Author Contents](#author-contents)
4. [Connect Contents with the Handbook](#connect-contents-with-the-handbook)
5. [Submit Pull Request](#submit-pull-request)

When contributing enhancements to an existing subject only part of these steps are 
relevant.

## Select a Subject

Think about a subject that is of interest to Software Engineers and from your own experience is not
covered well by existing tutorials or is not easily accessible.

Explore the [detailed Table of Contents (TOC)](TOC.md) to get ideas of such subjects and identify 
where your contribution may fit. If you think that the current TOC requires changes, we recommend 
that you open an issue that presents your change or fix, before submitting a pull request.

## Fork the Handbook Repository

Visit [Contributing to an Open Source Project][1] for instructions on how to fork and clone the 
[handbook repository on GitHub][2].

## Author Contents

### Prerequisites

Learn about the differences between [Guides](Guides) and [Topics](Topics) in the context of the 
Software Engineering Handbook.

Understand the [structure and conventions](README.md) used for the handbook.

### Guides and Topics Authoring

Create Guides and/or Topics for the selected subject. Include appropriate references to external 
sources with minimal duplications of exiting materials. Create internal links associating the 
set of Guides and Topics for the subject.

Your new contents is part of your local clone of the forked repository. Use [Git][3] to track the 
changes you are doing.

### Contents Style Guides

* Use [Markdown][4].
* See relevant examples in [Guides](Guides), [Topics](Topics), and 
  [config](config) directories.
* Use preview tools for Markdown

### Git Commit Messages Style Guides

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less

## Connect Contents with the Handbook

Compose at least one [Metadata configuration file](config/metadata) to connect the Handbook
navigation tree with the new contents. The [github.yml](config/metadata/github.yml) is a simple 
example of such configuration file, including a short introduction and references to GUides and 
Topics.

## Submit Pull Request

We use [GitHub Flow][5], which means all changes happen through [pull requests][1].

If you are a first time contributor, we recommend that you open an issue that presents your 
change or fix, before submitting a pull request.

---

[1]: http://software-engineering-handbook.com/Guides/Git/Contributing%20to%20an%20Open%20Source%20Project
[2]: https://github.com/uribench/software-engineering-handbook
[3]: http://software-engineering-handbook.com/Guides/Git/Git%20Overview
[4]: https://daringfireball.net/projects/markdown
[5]: https://guides.github.com/introduction/flow/index.html
