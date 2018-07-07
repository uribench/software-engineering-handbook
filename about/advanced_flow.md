# Advanced Workflow for Contributing to the Handbook

The following workflow describes the advanced steps required to contribute content for a new 
subject: 

1. [Select Subject](#select-subject)
2. [Set Development Environment](#set-development-environment) -- *optional step*
3. [Fork Handbook Repository](#fork-handbook-repository) -- *optional step*
4. [Create Content](#create-content)
5. [Connect Content with the Handbook](#connect-content-with-the-handbook) -- *optional step*
6. [Build Handbook](#build-handbook) -- *optional step*
7. [Submit Pull Request](#submit-pull-request)

Steps 2, 3, 5, and 6 above are the additional steps differentiating between this advanced workflow
and the [simple workflow](simple_flow.md). Any of these additional steps is **optional** and can be 
skipped at your own discretion. Skipped steps will be taken care by the repository moderator when 
reviewing your pull request.

When contributing enhancements to an existing subject only part of these steps are relevant.

## Select Subject

Think about a subject that is of interest to Software Engineers and from your own experience is not
covered well by existing tutorials or is not easily accessible.

Explore the [detailed Table of Contents (TOC)](toc.md) to get ideas of such subjects and identify 
where your contribution may fit. If you think that the current TOC requires changes, we recommend 
that you open an issue that presents your change or fix, before submitting a pull request.

## Set Development Environment

*This is an optional step*.

While developing your new content using this advanced workflow, it will be part of your local clone 
of the forked [handbook repository on GitHub][1].

Therefore, you have to set an environment that will allow you to conveniently edit content and 
use [Git][2] to track the changes you are doing and push the changes back to the fork on GitHub.

Following are several examples of common environments for Windows PC:

- [Git for Windows][3], ['Git Bash'][4] command window (bundled with Git for Windows)
- ['Git Bash'][4] command window, [Vagrant][5]
- [SSH Client][6], [Vagrant][5]

## Fork Handbook Repository

*This is an optional step*.
 
When skipped, this tep will be done automatically for you by GitHub if you create content directly 
on the GitHub repository using the 'Create new file' option, as in the 
[simple workflow](simple_flow.md).

Visit [Contributing to an Open Source Project][7] for instructions on how to fork and clone the 
[handbook repository on GitHub][1].

## Create Content

### Prerequisites

Learn about the differences between [Guides](Guides) and [Topics](Topics) in the context of the 
Software Engineering Handbook.

Understand the [structure and conventions](README.md) used for the handbook.

### Guides and Topics Authoring

Create Guides and/or Topics for the selected subject. Include appropriate references to external 
sources with minimal duplications of exiting materials. Create internal links associating the 
set of Guides and Topics for the subject. 

### Content Style Guides

* Use [Markdown][8].
* See relevant examples in [Guides](Guides), [Topics](Topics), and 
  [config](config) directories.
* Use preview tools for Markdown

### Git Commit Messages Style Guides

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less

## Connect Content with the Handbook

*This is an optional step*.

The Guides and Topics that you have created can be previewed directly. However, in order to make
them part of the Handbook you will have to connect them the Handbook navigation tree. This is done
by adding configuration one or more [Metadata configuration file](config/metadata).

The [github.yml](config/metadata/github.yml) is a simple example of such configuration file, 
including a short introduction and references to Guides and Topics.

## Build Handbook

*This is an optional step*.

At any time during the development of new content, you can build a new version of the handbook with
the new content placed under Guides, Topics, and config folders of your local clone of the forked 
handbook repository.

If you like, you can skip this step of building the complete handbook and reviewing it, and jump 
straight to submitting a pull request with the authored content. 

However, building and reviewing the complete handbook may help you identify issues prior to 
submitting a pull request.

If you decide to build the handbook, you will have to install the [handbook tools][9]. This is done 
easily with pip, which is a tool for installing Python packages.

The handbook tools are implemented in Python 3 as a command line and are available as a Pip package.

Make sure you have the Python 3 version of pip installed:

```bash
$ sudo apt upgrade python3-pip
```

Install the handbook-tools package:

```bash
$ pip3 install handbook-tools --user
```

The tools are used with a dispatcher called `handbook` that is executing dedicated commands in the
following pattern:

```bash
$ handbook [options] <command> [<args>...]
```

Run the following command to get help on the handbook tools usage:

```bash
$ handbook -h 
```

## Submit Pull Request

We use [GitHub Flow][9], which means all changes happen through [pull requests][7].

If you are a first time contributor, we recommend that you open an issue that presents your 
change or fix, before submitting a pull request.

---

[1]: https://github.com/uribench/software-engineering-handbook
[2]: http://software-engineering-handbook.com/Guides/Git/Git%20Overview
[3]: http://software-engineering-handbook.com/Guides/Git/Git%20Installation
[4]: http://software-engineering-handbook.com/Topics/Git%20Bash/
[5]: http://software-engineering-handbook.com/Guides/Vagrant/Vagrant%20Overview
[6]: http://software-engineering-handbook.com/Guides/SSH/Recommended%20SSH%20Clients
[7]: http://software-engineering-handbook.com/Guides/Git/Contributing%20to%20an%20Open%20Source%20Project
[8]: https://daringfireball.net/projects/markdown
[9]: https://github.com/uribench/software-engineering-handbook-tools
[10]: https://guides.github.com/introduction/flow/index.html
