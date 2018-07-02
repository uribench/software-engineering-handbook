# Working with a Remote Git Repository

For collaboration, you may like to go beyond working with a local [Git][1] repository. Technically, 
you can push changes to and pull changes from remote repositories on individuals' computers using 
one of the supported [protocols](#protocols). However, a more reliable and effective way for 
collaboration is working with a hosted common repository on a server. [GitHub][2] is a popular such 
host for Git repositories.

## Protocols

We will not discuss here the **local protocol**, the older **'dumb' HTTP protocol**, or the **Git 
protocol** that relies on a special daemon running locally. You can read about these protocols on 
the [Pro Git book][2].

We will rather focus on the newer **'smart' HTTP protocol** and on the **SSH protocol** that are 
widely used for accessing remote Git repositories.

## Authentication

Assuming you have an account and a repository on a remote Git repository server, you have to 
authenticate yourself in order to gain access to the server. 

With the simpler to use HTTP protocol, you use username and password for authentication. However,
the [SSH protocol][4] employs public key cryptography for authentication using public and 
private SSH key pair with an asymmetric encryption method. See [How Does SSH Works][5] for details 
on SSH session stages and their encryption technologies.

Before you can authenticate using the SSH protocol you need to do the following:

- [Generate an SSH key pair][6]
- Set an [authentication agent][7]
- Share the public key with the server (see [an example on how to do that with GitHub][8])

From this point on, the authentication is handled on your behalf by the authentication agent.

## Common Commands for Working with a Remote Git Repository

Justing James provides about 1 hour [Intro to Version Control with Git and GitHub][9] on YouTube. 

For more details, see the comprehensive set of [guides for using GitHub][10].

Following is a brief description of the most common commands for working with Git and GitHub as the 
remote repository. To use these commands you have to have [Git installed][11] and be familiar with 
the [basic use of Git][12]:

- Pushing an existing local repository to a remote repository
- Committing changes to a remote repository
- Renaming a file on a local repository and pushing the change to a remote repository
- Managing a remote repository
- Pulling changes you or other people did on the remote repository
- Cloning: getting a local copy of a remote repository
- Contributing to an open source project using Git and GitHub

### Pushing an Existing Local Repository to a Remote Repository

The **first time** you push an existing local repository to a remote repository you first have to 
define the 'origin' as a remote repository. This needs to be done once only for each repository. 

The command for defining the 'origin' depends on the [protocol](#protocols) being used. Note that 
this command does not yet send the local repository to remote server.

**When using the HTTP Protocol:**

```bash
$ git remote add origin https://github.com/<your_gitub_user_name>/<repo_name>.git

Example: 
$ git remote add origin https://github.com/uribench/software-engineering-handbook-tools.git
```

**When using the SHH Protocol:**

```bash
$ git remote add origin git@github.com:<your_gitub_user_name>/<repo_name>.git

Example: 
$ git remote add origin git@github.com:uribench/software-engineering-handbook-tools.git
```

From that point on, the command to send the local repository to the remote server does not depend on
the protocol.

```bash
$ git push -u origin master

Output Example:
    Counting objects: 7, done.
    Delta compression using up to 4 threads.
    Compressing objects: 100% (7/7), done.
    Writing objects: 100% (7/7), 17.28 KiB | 2.16 MiB/s, done.
    Total 7 (delta 1), reused 0 (delta 0)
    remote: Resolving deltas: 100% (1/1), done.
    To https://github.com/uribench/software-engineering-handbook-tools.git
     * [new branch]      master -> master
    Branch 'master' set up to track remote branch 'master' from 'origin'.
```

Notes:

1. The `-u` flag tells Git to set a tracking reference to the remote branch. This defines the
   'origin' as the default tracking reference to the remote branch. Needs to be done only the
   first time you use the 'git push' command for a repository. Change 'master' to whatever 
   branch you want to push your changes to.
2. When using the HTTP Protocol, you may be prompted on the local PC to login into your GitHub 
   account.
3. When using the HTTP Protocol, you may be prompted on the local PC to provide the passphrase for 
   your SSH Key.

Sending a local repository to remote **after the first time**:

```bash
$ git push
```

Notes: 

1. There is no need to specify the `-u` flag and explicitly specify the tracking reference to the 
remote branch.
2. You can check the remote repository in GitHub online.

### Committing Changes to a Remote Repository

1. Make changes and commit them locally: `$ commit -m "<message>"`
2. Check status to see that the commit was successful: `$ git status`
3. Push local repository to the respective remote repository on GitHub: `$ git push`
   Note: Unlike the first time we did push, here we do not need the `-u` flag with the explicit 
   specification of the tracking reference to the remote branch. It is already known.
4. Check status to see that the push was successful: `$ git status`

### Pulling Changes you or other People did on the Remote Repository

1. First commit your local changes, otherwise your changes will be overwritten by the pulled changes:
    `$ git commit -m "<message>"`
2. Pull changes other people have made: `$ git pull`
3. Fix any conflicts locally and commit locally: `$ git commit -m "<message>"`
4. Push the updated local repository to the remote repository: `$ git push`

### Renaming a File on a Local Repository and Pushing the Change to a Remote Repository

**Step 1: Rename the file using Git, specifying the old file name and the new name you'd like to 
give the file.**  

```bash
$ git mv <old_filename> <new_filename>

Example:
$ git mv Readme.md README.md
```

Note: This will stage your change for commit.

**Step 2: Check the repository status:**

```bash
$ git status
Output Example:
    On branch master
    Your branch is up to date with 'origin/master'.

    Changes to be committed:
      (use "git reset HEAD <file>..." to unstage)

    renamed:    Readme.md -> README.md
```

**Step 3: Commit the file that you've staged in your local repository:**

```bash
$ git commit -m "Rename file"
Output Example:
    [master 6c93564] Rename file
     1 file changed, 0 insertions(+), 0 deletions(-)
     rename Readme.md => README.md (100%)
```

**Step 4: Push the changes in your local repository to GitHub:**

```bash
$ git push
Output Example:
    Counting objects: 2, done.
    Delta compression using up to 4 threads.
    Compressing objects: 100% (2/2), done.
    Writing objects: 100% (2/2), 224 bytes | 224.00 KiB/s, done.
    Total 2 (delta 1), reused 0 (delta 0)
    remote: Resolving deltas: 100% (1/1), completed with 1 local object.
    To https://github.com/uribench/SheetProperties.git
       77c1868..6c93564  master -> master
```

### Managing a Remote Repository

**Deleting a file or directory from a remote repository:**

```bash
$ git rm -r --cached <directory_name or file_name>
$ git commit -m "Remove directory (or file) '<directory_name or file_name>'"
$ git push
```

**Changing the GitHub repository name can be done as follows:**

1. Log into your Github account.
2. Go into 'Settings'
3. Modify the repository name and press 'Rename'
4. In the local repository change the name of the project directory (the one containing .git folder), 
accordingly.
5. In the local repository open `./git/config` file for editing
6. Replace the value of the 'url' key in the `[remote "origin"]` block to point to the repository 
with the new name.
7. Check that the above actions were successful by issuing the following command locally:  
   `$ git remote -v`

### Cloning: Getting a Local Copy of a Remote Repository

1. Move to a folder that is supposes to be the parent of a new folder to be created automatically by 
   Git for the clone of the remote repository:  
   `$ cd <parent_of_the_future_project_folder>`
2. Create a local clone of a remote repository:  
   `$ git clone https://github.com/<your_gitub_user_name>/<repo_name>.git`
3. Move to the newly created folder containing the clone:  
   `$ cd <repo_name>`
   Note: The `<repo_name>` folder has been created automatically by Git to store the clone of the 
   remote repository.

### Contributing to an Open Source Project using Git and GitHub

Read instruction in [Contributing to an Open Source Project][13].

---

[1]: /Guides/Git/Git%20Overview
[2]: /Topics/GitHub
[3]: https://git-scm.com/book/en/v2/Git-on-the-Server-The-Protocols
[4]: /Topics/SSH%20Protocol
[5]: /Topics/SSH%20Protocol/How%20Does%20SSH%20Work
[6]: /Guides/SSH/Generating%20an%20SSH%20Key%20Pair
[7]: /Guides/SSH/Managing%20SSH%20Keys
[8]: https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/
[9]: https://www.youtube.com/watch?v=KXKVA0mMihU&feature=youtu.be
[10]: https://guides.github.com/
[11]: /Guides/Git/Git%20Installation
[12]: /Guides/Git/Getting%20Started%20with%20Git
[13]: /Guides/Git/Contributing%20to%20an%20Open%20Source%20Project

