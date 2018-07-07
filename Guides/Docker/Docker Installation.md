# Docker Installation

The [Docker][1] installation instructions provided here are specific to Linux, either as a native 
OS, or hosted as a Virtual Machine (VM). 
You can create and run a Linux VM on a Windows PC using [Vagrant][2].

Following are detailed steps for installing Community Edition Docker (Docker CE) on Linux using the 
recommended approach. This approach and one more approach are described by the Docker official
documentation in [Get Docker CE for Ubuntu][3].

A short note about the [Advanced Package Tool][4] (APT) may help understand why the below initial 
installation process is lengthy, and why updating the installation later can be done using a single 
command.

APT relies on the concept of repositories in order to find software and resolve dependencies. For 
APT, a repository is a directory containing packages along with an index file. The Debian project 
keeps a central repository of over 25,000 software packages ready for download and installation. Any 
number of additional repositories can be added to APT's `sources.list` configuration file 
(`/etc/apt/sources.list`) and then be queried by APT.

## Install Docker

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
image found on the [Docker Hub][5].

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

If you would like later to update Docker, just repeat steps 2.1 and 2.2.

## Creating Directory Structure for Docker Projects

Before or after installing Docker, create a directory structure in Windows for Docker projects.

The following structure extends the [recommended directory structure for the Vagrant Boxes][6] to 
include Docker projects:

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

In the above structure, each docker project has its own [Dockerfile][7].

---

**Related Guides:**

- [Docker Overview][1]
- [Getting Started with Docker][10]

---

[1]: /Guides/Docker/Docker%20Overview
[2]: /Guides/Vagrant/Vagrant%20Overview
[3]: https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce
[4]: https://manpages.debian.org/stretch/apt/apt.8.en.html
[5]: https://hub.docker.com/
[6]: /Guides/Vagrant/Vagrant%20Installation#creating-directory-structure-for-vagrant-boxes
[7]: /Topics/Dockerfile

[10]: /Guides/Docker/Getting%20Started%20with%20Docker