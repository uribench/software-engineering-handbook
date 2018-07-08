# Detailed Docker Installation

The following annotated [Docker][1] installation instructions are based the Docker official 
documentation in [Get Docker CE for Ubuntu][2].

For a short version see [Docker Installation][3].

Using the instruction provided here require Linux. You can create and run a Linux VM on a Windows PC 
using [Vagrant][4].

A short note about the [Advanced Package Tool][5] (APT) may help understand why the below initial 
installation process is lengthy, and why updating the installation later can be done using a single 
command.

APT relies on the concept of repositories in order to find software and resolve dependencies. For 
APT, a repository is a directory containing packages along with an index file. The Debian project 
keeps a central repository of thousands of software packages ready for download and installation. 
Any number of additional repositories can be added to APT's `sources.list` configuration file 
(`/etc/apt/sources.list`) and then be queried by APT.

## Install Docker on Debian based Linux distributions

Two main steps are required in order to install Docker CE:

- [Update the Known Repositories of APT](#update-the-known-repositories-of-apt)
- [Install Docker CE from a Known Repository](#install-docker-ce-from-a-known-repository)

### Update the Known Repositories of APT

**Step 1.1: Update the apt package index:**

```bash
$ sudo apt update
```

**Step 1.2: Upgrade upgradeable packages:**

This is an optional step. If you are prompted after the previous command that there are packages 
that can be upgraded, you may decide to list them and upgrade them using the following commands:

```bash
$ apt list --upgradable
$ sudo apt upgrade 
```

**Step 1.3: Install required packages:**

Install packages to allow apt to use a repository over HTTPS.

```bash
$ sudo apt install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
```

You may be prompt that one or more of he above packages have already the newest versions installed.

**Step 1.4: Add Docker’s official key:**

Add Docker’s official GNU Privacy Guard (GnuPG. Also knows as GPG) key.

```bash
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

**Step 1.5: Verify the GPG key:**

Verify that you have now the key with the fingerprint 
`9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88`, by searching for the last 8 characters of 
the fingerprint.

```bash
$ sudo apt-key fingerprint 0EBFCD88
```

**Step 1.6: Set up the 'stable' repository:**

If you need also 'edge' or 'test' repositories add the word `edge` or `test` (or both) after the 
word `stable` in the commands below.

```bash
$ sudo add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) \
    stable"
```

### Install Docker CE from a Known Repository

**Step 2.1: Update the apt package index:**

```bash
$ sudo apt update
```

**Step 2.2: Install the latest version of Docker CE:**

```bash
$ sudo apt install docker-ce
```

**Step 2.3: Add yourself to the docker group:**

This is done, so `sudo` command will not be needed for docker commands.

```bash
$ sudo usermod -aG docker $USER
```

Logging out and logging back in is required, because the group change will not have an effect unless 
your session is closed.

**Step 2.4: Verify that Docker CE is installed correctly:**

Verify that Docker CE is installed correctly by running a Docker container from the 'hello-world' 
image found on the [Docker Hub][6].

```bash
$ docker run hello-world
```

If all goes well, you are supposed to get something similar to the following message:

```bash
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
9bb5a5d4561a: Pull complete

...more text...

Hello from Docker!
This message shows that your installation appears to be working correctly.
```

## Update Docker

If you would like later to update the installed Docker, just repeat the above Steps 2.1 and 2.2.

## Creating Directory Structure for Docker Projects

At some point, before or after installing Docker, you will have to create a directory structure for 
Docker projects.

The following structure is an example of such structure on Windows. It is not provided here as the
best structure or as the only possible structure. This is just a possible example that extends the 
[example directory structure for Vagrant based projects][7] to include Docker projects:

```
Drive:\                                   For instance D:\
└──Vagrant\                               Main location of the Vagrant Boxes
   ├──guest_os_name\                      The guest OS for all child projects (e.g., xenial) 
   |  ├──.vagrant\                        Created automatically on the first launch of vagrant
   |  ├──some_vagrant_project_name\       Directory for a project using the same guest OS 
   |  ├──another_vagrant_project_name\    Another project directory using the same guest OS
   |  ├──docker\                          Directory for docker projects
   |  |  ├──some_docker_project_name\     Directory for docker project using the same guest OS  
   |  |  |  ├──project_files
   |  |  |  └──Dockerfile
   |  |  └──another_docker_project_name\  Another docker project directory using the same guest OS
   |  |     ├──project_files
   |  |     └──Dockerfile
   |  └──Vagrantfile                      Common vagrant config. file for projects in this directory
   └──another_guest_os_name\              Optional: Another guest OS for the child projects 
```

In the above structure, each docker project has its own [Dockerfile][8].

---

**Related Guides:**

- [Docker Overview][1]
- [Getting Started with Docker][9]

---
[1]: /Guides/Docker/Docker%20Overview
[2]: https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce
[3]: /Guides/Docker/Docker%20Installation
[4]: /Guides/Vagrant/Vagrant%20Overview
[5]: https://manpages.debian.org/stretch/apt/apt.8.en.html
[6]: https://hub.docker.com/
[7]: /Guides/Vagrant/Vagrant%20Installation#creating-directory-structure-for-vagrant-boxes
[8]: /Topics/Dockerfile
[9]: /Guides/Docker/Getting%20Started%20with%20Docker