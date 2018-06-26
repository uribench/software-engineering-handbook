# Getting Started with Git

Git has [three main states][1] that your files can reside in:

- **Committed** means that the data is safely stored in your local database.
- **Modified** means that you have changed the file but have not committed it to your database yet.
- **Staged** means that you have marked a modified file in its current version to go into your 
next commit snapshot.

This leads to the three main sections of a **Git project**:

- **Working directory** - including the project tree (a single checkout of one version of the 
project).
- **Git directory** - included in the Project directory.
- **Staging area** - generally contained as an index file in the Git directory.

## Table of Contents

- [Basic Workflow](#basic-workflow)
- [Basic Workflow Git Commands](#basic-workflow-git-commands)
- [Additional Common Commands](#additional-common-commands)
- [Typical Recovery Commands](#typical-recovery-commands)
- [Ignoring Files](#ignoring-files)
- [Branching and Merging](#branching-and-merging)
- [Tagging](#tagging)


## Basic Workflow

The basic Git workflow typically involves the following steps, after creating the initial repository:

1. Modify files in your working tree.
2. Selectively stage changed files for the next commit.
3. Commit the staged files to be tracked by Git.

Next sections provide kind of 'cheat sheet' for common Git commands.


## Basic Workflow Git Commands

All the following commands have to be executed from the root of the Project directory.

```bash
# Create an empty Git repository or reinitialize an existing one
# Note the newly created './.git' folder
$ git init

# Add (stage) all files and directories in the project folder to the index
$ git add . --all

# Record (commit) changes to the repository with a message
$ git commit -m "commit message"
```

## Additional Common Commands

Commands for common "housekeeping" tasks are provided below.

```bash
# Show the working tree status. Use it frequently before and after staging and committing.
$ git status

# Show commit logs history
$ git log

# Show prettier commit logs
$ git log --oneline --graph --decorate

# Show changes between commits, commit and working tree, etc.
$ git diff
$ git diff <tag(or)branch name>
$ git diff <path/to/file_name (or) path/to/folder>
$ git diff <tag1(or)branch1 name> <tag2(or)branch2 name>

# Show changes using common diff tools
# Note: All 'git diff' arguments and options are applicable here too
$ git difftool

```

## Typical Recovery Commands

Occasionally, you may want to recover several situations at various Git states as follows.

```bash
# Undoing local changes on a file before staging the file and before committing the new changes
# Note: This will replace the uncommitted file with the one from the repository
$ git checkout <file_name>

# Undoing local changes on a file after staging the file and before committing the new changes
$ git reset HEAD <file_name>
# Note: After that, if you like, you may checkout the committed version using
$ git checkout <file_name>

# Undoing local changes on a file after staging the file and after committing the new changes
# Note: This actually is not removing the latest commit, it just does checkout of the revision 
# pointed by <HASH>, and commit it as the newest commit (becoming the HEAD). All the historical 
# revisions remain in Git. It is done so, in order to protect other developers that are depending 
# on the revision that was "undone".
$ git revert <HASH>

# Alternatively, same as above but without making the commit
$ git revert --no-commit <HASH>

# Correcting the last commit message (e.g., in case of Typo):
# Notes: 
#   1. This will actually replace the tip of the current branch by creating a new commit.
#   2. You should understand the implications of rewriting history if you amend a commit that has 
#      already been published.
$ git commit -m "Corrected Message" --amend

# Deleting a new file after staging the file and before committing it.
# Note: This will remove the file from the staging list and it will not be committed automatically
# on the next commit. You can look at 'git rm' as the inverse command of 'git add'.
$ git rm <file_name>

# Deleting a file or directory after staging the file and after committing it
$ git rm -r --cached <directory_name or file_name>
$ git commit -m "Remove directory (or file) '<directory_name or file_name>'"

# Checkout a single file from a specific commit pointed by <HASH>
$ git checkout <HASH> <path/to/the/messed/up/file>
```

## Ignoring Files

A gitignore file specifies intentionally untracked files that Git should ignore. Note that files 
already tracked by Git are not affected.

Git requires a text file called '.gitignore' in the project folder. It lists the files to be ignored 
by Git. Make sure to also commit the '.gitignore' file itself.

The '.gitignore' may include any of the following patterns:

```
# Single specific file
<folder_name>/<file_name>

# Directory list with all the contained files
<folder_name1>
<folder_name2>

# Wildcard
*.<extension>
```

## Branching and Merging

Branching is a common way to develop different code on the same base. It is useful for exploratory 
work (e.g., POC) without affecting master branch. Anything done inside this branch is not affecting 
anything else outside this branch. When ready, merge changes back into the master branch. Do the 
merge as frequently as possible.

Following are common commands for creating and managing branches:

```bash
# Creating a new branch named <new_branch_name>
# Notes: 
#   1. After the new branch is created and the files were checked out, Git tracks the new branch.
#   2. You can commit the new changes on the new branch as usual. They will be separated from the 
#      master.
$ git checkout -b <new_branch_name>

# Listing available branches: Local branches only
$ git branch
# Example:
#   $ git branch
#   Output:
#       master
#       *featureABC
# Note: The '*' in front of a branch name indicates it is the active branch.

# Listing available branches: Both local and remote branches
$ git branch -a

# Switching branches (to one that already exists after committing the changes of the current branch)
$ git checkout <branch_name>
# Example:
#   $ git branch
#   Output:
#       master
#       *featureABC
#   $ git checkout master
#   Output:
#       Switched to branch 'master'

# Merging a branch back into the master branch (after committing the changes of the current branch)
# Note: First checkout the branch you want to merge into (in this case it is 'master')
$ git checkout master
$ git merge <branch_name>

# Note: Before merging changes, you can also preview them
$ git diff <source_branch> <target_branch>
```

Merging conflicts: When there is a conflict between lines in files of the two branches, the 
automatic merge will fail.
If you run `git status` command, you get a list of un-merged paths.
The files containing the conflicts will have hints embedded in them by Git.
Fix the conflicts and commit the changes, or abort the merge by:

```bash
$ git merge --abort
```

Removing a branch after merging it:

```bash
# Deleting locally
$ git branch -d <branch_name>
```

## Tagging

It is recommended to create tags for software releases. This is a known concept, which also exists in SVN.

```bash
# Annotated Tag: Creating an annotated tag in Git is simple. The easiest way is to specify -a when 
# you run the 'tag' command
$ git tag -a <tag> -m "message"
# Example:
#   $ git tag -a v1.0.0 -m "my version 1.0.0"

# Lightweight Tag: Another way to tag commits is with a lightweight tag. To create a lightweight 
# tag, don’t supply any of the -a, -s, or -m options, just provide a tag name
$ git tag <tag>

# You can also tag commits after you’ve moved past them. To tag that commit, you specify the commit 
# checksum (or part of it) at the end of the command
$ git tag <tag> <HASH>
# Example for a tag named v1.0.0 for commit 1b2e1d63ff:
#   $ git tag v1.0.0 1b2e1d63ff
#   Notes: The 1b2e1d63ff stands for the first 10 characters of the commit id you want to reference 
#   with your tag (you can use less than 10 characters too). You can get the commit id by looking at 
#   the log.

# Listing the available tags in Git
$ git tag

# You can see the tag data along with the commit that was tagged by using the git show command
$ git show <tag>

# Listing the commits log with their tags and commit messages (one line for each commit)
$ git log --oneline --decorate --graph

# Rename old tag:
# First you need to build an alias of the old tag name
$ git tag new_tag_name old_tag_name
# Then you need to delete the old one locally
$ git tag -d old_tag_name
# Notes:
#   1. Although it can be done, it is not recommended to rename tags of a commit that was published.
#   2. If a tag is annotated, the new tag won't have the message of the old one.
```

---

**Related Guides:**

- [Git Overview][2]
- [Git Installation][3]

---

[1]: https://git-scm.com/book/en/v2/Getting-Started-Git-Basics
[2]: /Guides/Git/Git%20Overview
[3]: /Guides/Git/Git%20Installation
