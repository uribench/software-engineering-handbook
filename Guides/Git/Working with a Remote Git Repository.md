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

Justing James provides about 1 hour [Intro to Version Control with Git and Github][9] on YouTube. 

For more details, see the comprehensive set of [guides for using GitHub][10].

Following is a brief description of the most common commands for working with GitHub as the remote 
repository:

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
2. You can check the remote repository in Github online.

### Committing Changes to a Remote Repository

### Renaming a File on a Local Repository and Pushing the Change to a Remote Repository

### Managing a Remote Repository

### Pulling Changes you or other People did on the Remote Repository

### Cloning: Getting a Local Copy of a Remote Repository

### Contributing to an Open Source Project using Git and GitHub

---

[1]: /Guides/Git/Git%20Overview
[2]: /Topics/GitHub
[3]: https://git-scm.com/book/en/v2/Git-on-the-Server-The-Protocols
[4]: /Topics/SSH%20Protocol
[5]: /Topics/SSH%20Protocol/How%20Does%20SSH%20Work
[6]: Guides/SSH/Generating%20an%20SSH%20Key%20Pair
[7]: Guides/SSH/Managing%20SSH%20Keys
[8]: https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/
[9]: https://www.youtube.com/watch?v=KXKVA0mMihU&feature=youtu.be
[10]: https://guides.github.com/
