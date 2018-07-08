# Docker Installation

The [Docker][1] installation instructions provided here are specific to Debian based Linux 
distributions, such as Ubuntu, either as a native OS, or hosted on a Virtual Machine (VM). 

The following steps for installing the Community Edition Docker (Docker CE) on Linux summarize 
the recommended approach by the Docker official documentation in [Get Docker CE for Ubuntu][2].

For annotated instructions with explanations see the [detailed docker installation instructions][3].

## Update the Known Repositories of APT

**Step 1.1: Update the apt package index:**

```bash
$ sudo apt update
```

**Step 1.2: Install required packages:**

```bash
$ sudo apt install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
```

**Step 1.3: Add Docker’s official GNU Privacy Guard key (GPG):**

```bash
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

**Step 1.4: Verify the GPG key:**

```bash
$ sudo apt-key fingerprint 0EBFCD88
```

**Step 1.5: Set up the 'stable' repository:**

```bash
$ sudo add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) \
    stable"
```

## Install Docker CE from a Known Repository

**Step 2.1: Update the apt package index:**

```bash
$ sudo apt update
```

**Step 2.2: Install the latest version of Docker CE:**

```bash
$ sudo apt install docker-ce
```

**Step 2.3: Add yourself to the docker group:**

```bash
$ sudo usermod -aG docker $USER
```

**Step 2.4: Verify that Docker CE is installed correctly:**

```bash
$ docker run hello-world
```

## Update Docker

If you would like later to update the installed Docker, just repeat the above Steps 2.1 and 2.2.

---

**Related Guides:**

- [Docker Overview][1]
- [Getting Started with Docker][4]

---

[1]: /Guides/Docker/Docker%20Overview
[2]: https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce
[3]: /Guides/Docker/Detailed%20Docker%20Installation
[4]: /Guides/Docker/Getting%20Started%20with%20Docker