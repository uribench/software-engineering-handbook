# Docker Overview

[Docker][1] provides a way to run applications securely isolated in a container, packaged with all 
its dependencies and libraries.

The traditional way of virtualization, sometimes called full virtualization, allows an unmodified 
Operating System (OS) with all of its installed software to run in a special environment on top of  
the existing operating system. This environment is called **Virtual Machine** (VM). The physical 
computer is then usually called the **Host**, while the virtual machine is often called a **Guest**.
Multiple guest VMs, each with its own guest OS, can run on a single host OS.

Linux Containers, on the other hand, run in user space on top of the kernel of the host OS. This is 
called OS level virtualization. Multiple containers can run on a single host, each having its own 
user space, this means even different Linux systems. 

Since containers do not have their own kernel, they share the kernel of the host OS. This makes them 
much smaller in size compared to virtual machines. Moreover, containers are less resource intensive, 
offer better performance, quicker to provision, and easy to scale, compared to virtual machines.

A common solution for running Linux Containers on a native Windows computer is to install a Linux VM 
on top of the Windows system. This Linux VM, which is a guest OS on the native Windows host OS, can 
then serve as a host OS for containers by providing its kernel to the hosted containers.

Docker offers a standard way to build out a container workload so that it could be moved around and 
still run in a predictable way in any container-ready environment.

Following are [definitions][2] of fundamental terminology used with Dockers.

## Docker Image

A Docker image is a read-only template with instructions for creating a 
[Docker container](#docker-container). 
Often, an image is based on another image, with some additional customization. For example, you may 
build an image which is based on the ubuntu image, but installs the Apache web server and your 
application, as well as the configuration details needed to make your application run.

You might create your own images or you might only use those created by others and published in a 
registry, such as the [Docker Hub][3]. To build your own image, you create a [Dockerfile][4] with a 
simple syntax for defining the steps needed to create the image and run it.

## Docker Container

A Docker container is a runnable instance of a [Docker image](#docker-image). You can create, start, 
stop, move, or delete a container using the Docker API or CLI. You can connect a container to one or 
more networks, attach storage to it, or even create a new image based on its current state.

By default, a container is relatively well isolated from other containers and its host machine. You 
can control how isolated a container’s network, storage, or other underlying subsystems are from 
other containers or from the host machine.

A container is defined by its image as well as any configuration options you provide to it when you 
create or start it. When a container is removed, any changes to its state that are not stored in 
persistent storage disappear.

## Docker Client and Daemon

Docker uses a client-server architecture. The Docker daemon is responsible for building, running, 
and distributing the Docker containers. The Docker client interacts with one or more Docker daemons 
to carry out a Docker task, by sending commands such as `docker run`. The Docker client and daemon 
can run on the same or on different systems.

## Docker Registries

Docker registry is a repository for Docker images. [Docker Hub][3], as an example, is such a public 
registry with thousands of images created by users that anyone can use. It is configured by Docker 
as the default source of images. 

Working with Docker Hub can be viewed as similar to working with git and GitHub. You can build and 
commit an image locally, and then push it to the Docker hub. If your repository is public, all your 
images can be accessed by other Docker hub users. You can also create a private registry in Docker 
Hub.

When you use the `docker pull` or `docker run` commands, the required images are pulled from your 
configured registry. When you use the `docker push` command, your image is pushed to your configured 
registry.

---

**Related Guides:**

- [Docker Installation][5]
- [Getting Started with Docker][6]

---

[1]: https://docs.docker.com/
[2]: https://docs.docker.com/engine/docker-overview/#docker-objects
[3]: https://hub.docker.com/
[4]: /Topics/Dockerfile
[5]: /Guides/Docker/Docker%20Installation
[6]: /Guides/Docker/Getting%20Started%20with%20Docker

