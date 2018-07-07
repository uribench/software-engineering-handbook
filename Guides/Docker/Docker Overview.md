# Docker Overview

[Docker][1] provides a way to run applications securely isolated in a container, packaged with all 
its dependencies and libraries.

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

