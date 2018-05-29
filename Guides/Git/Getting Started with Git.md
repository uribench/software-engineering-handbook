# Getting Started with Git

Git has [three main states][1] that your files can reside in:

> - **Committed** means that the data is safely stored in your local database.
> - **Modified** means that you have changed the file but have not committed it to your database yet.
> - **Staged** means that you have marked a modified file in its current version to go into your 
next commit snapshot.

This leads to the three main sections of a **Git project**:

- **Working directory** - including the project tree (a single checkout of one version of the 
project)
- **Git directory** - included in the Project directory
- **Staging area** - generally contained as an index file in the Git directory


## Basic Workflow

The basic Git workflow typically involve the following steps, after creating the initial repository:

1. Modify files in your working tree.
2. Selectively stage changed files for the next commit.
3. Commit the staged files to be tracked by Git.

Next sections provide kind of 'cheat sheet' for common Git commands.


### Basic Workflow Git Commands

All the following commands has to be executed from the root of the Project directory.

Command                            | Description/Comment
-----------------------------------|----------------------------------------------------------------
`$ git init`<br>                   | Create an empty Git repository or reinitialize an existing one
`$ git add . --all`                | Add (stage) all files/dirs in the project folder to the index
`$ git commit -m "commit message"` | Record (commit) changes to the repository with a message

## Additional Common Commands

### Checking Status

### Viewing Commits Log

### Comparing Files


## Typical Recovery Commands

## Ignoring Files

## Branching

## Tagging



---

**Related Guides:**

- [Git Overview][2]
- [Git Installation][3]

---

[1]: https://git-scm.com/book/en/v2/Getting-Started-Git-Basics
[2]: /Guides/Git/Git%20Overview
[3]: /Guides/Git/Git%20Installation
