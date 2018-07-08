# Getting Started with Docker

Once the [Docker][1] has been [installed][2], it is ready to be used. All the following instructions
are intended to be used from a native Linux or from a Linux VM. If you are using a Linux VM under 
[Vagrant][3], it is assumed you know how to use a [Vagrant VM][4] (i.e., control its life-cycle and 
connect with a running Vagrant VM).

Only the most common Docker CLI commands are introduced here. For a complete list and more details 
visit the Docker official documentation in [Use the Docker command line][5]

## Table of Contents:

- [Build a Docker Image from Dockerfile](#build-a-docker-image-from-dockerfile)
- [Create a Docker Container from Docker Image](#create-a-docker-container-from-docker-image)
- [Run a Docker Container](#run-a-docker-container)
- [Stop a Running Docker Container](#stop-a-running-docker-container)
- [Manage Local Docker Images and Containers](#manage-local-docker-images-and-containers)
    - [List Local Docker Images](#list-local-docker-images)
    - [Remove Local Docker Images](#remove-local-docker-images)
    - [List Containers](#list-containers)
    - [Clean Docker Containers Space](#clean-docker-containers-space)
- [Share Files between Host Machine and Docker Container](#share-files-between-host-machine-and-docker-container)

## Build a Docker Image from Dockerfile

To build a [Docker image][6] from a [Dockerfile][7] use: [`docker image build PATH | URL`][8].

Where `PATH | URL` are two alternatives to specify the location of the Dockerfile.

## Create a Docker Container from Docker Image

To create a new Docker container from a Docker Image use:
[`docker create [OPTIONS] IMAGE [COMMAND] [ARG...]`][9]

This creates a writeable container layer over the specified image and prepares it for running the 
specified command. 

## Run a Docker Container 

To run a Docker container from a Docker image use: [`docker run [OPTIONS] IMAGE`][10].

Where IMAGE is a local image or a remote pre-built image, as in the following two examples.

### Use pre-built Docker Images

Following are instructions for using two common pre-built Docker images:

- [alpine Docker image][11]
- [ubuntu Docker image][12]

These above two containers will be downloaded automatically from their respective official 
repositories on [Docker Hub][13].

#### Use alpine Docker Image

The `alpine` is a minimal Docker image based on 'Alpine Linux' with a complete package index and 
only 5 MB in size.

Run the following command to create a container based on the `alpine` Docker image, and enter an 
`sh` simple terminal in it:

```bash
$ docker run -it --rm alpine sh
```

Note that the above `docker run` command includes the following parts:
    -i, --interactive       Keep STDIN open even if not attached (run the container interactively)
    -t, --tty               Allocate a pseudo-TTY (attach the container to the terminal)
    --rm                    After exiting the docker, remove the container
    alpine                  The tag name of the docker image to run
    sh                      The command to enter (here it is 'sh' simple terminal)

#### Use ubuntu Docker Image

The 'ubuntu' Docker image is based on 'Ubuntu Linux', which is a Debian-based Linux operating system 
based on free software.

Run the following command to create a container based on the `ubuntu` Docker image and enter a 
`bash` terminal in it:

```bash
$ docker run -it ubuntu /bin/bash
```

When you run this command, the following happens (assuming you are using the default registry 
configuration):

1. If you do not have the ubuntu image locally, Docker pulls it from your configured registry, 
   as though you had run `docker pull ubuntu` command manually.
2. Docker creates a new container, as though you had run a `docker container create` command 
   manually.
3. Docker allocates a read-write filesystem to the container, as its final layer. This allows a 
   running container to create or modify files and directories in its local filesystem.
4. Docker creates a network interface to connect the container to the default network, since you 
   did not specify any networking options. This includes assigning an IP address to the container. 
   By default, containers can connect to external networks using the host machine’s network 
   connection.
5. Docker starts the container and executes `/bin/bash`. Because the container is run interactively 
   and attached to your terminal (due to the -i and -t) flags, you can provide input using your 
   keyboard and output is logged to your terminal.

When you type exit to terminate the '/bin/bash' command, the container stops but is not removed. 
You can start it again or remove it.

## Stop a Running Docker Container

To stop and exit a Docker container press Ctrl-D or use the `logout` command.

## Manage Local Docker Images and Containers

### List Local Docker Images

To list all the docker images (those that were built or pulled as pre-built):

```bash
$ docker images -a
```

Example output:

```bash
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
alpine              latest              11cd0b38bc3c        46 hours ago        4.41MB
ubuntu              latest              113a43faa138        4 weeks ago         81.2MB
hello-world         latest              e38bc07ac18e        2 months ago        1.85kB
```

Notes: 

1. Watch the difference between the size of `alpine` and `ubuntu` images.
2. We run the `hello-world` image on the last stage of [Docker installation][2] to verify it was
   installed correctly. 

### Remove Local Docker Images

To remove a docker image use the following command:

```bash
$ docker rmi [-f] <image_id>
```

Example:

```bash
$ docker rmi 3fd9065eaf02
```

### List Containers

To list all containers (show all containers, not just running):

```bash
$ docker ps -a
```

Example output:

```bash
CONTAINER ID      IMAGE           COMMAND         CREATED          STATUS
8fb2eaaa1f41      ubuntu          "/bin/bash"     5 minutes ago    Exited (0) 5 minutes ago
c6e037f1ae3f      hello-world     "/hello"        18 hours ago     Exited (0) 18 hours ago
```

Note: The container that we created above based on `alpine` is not listed. This is because we used 
the `--rm` option of the `docker run` command.

### Clean Docker Containers Space

To clean all space occupied by Docker containers (temporary images, containers, network, volumes...)

```bash
$ docker system prune -f
```

After executing the above command, the `$ docker ps -a` yields an empty list of containers.

Note: Don't worry, you can create and run a new container very fast (assuming the Dockerfile has 
not changed) from an existing image (check with `docker images` command) by using the 
`docker create` or `docker run` commands. More on that in the next sections.

## Share Files between Host Machine and Docker Container

There are several ways to pass files between the host machine (aka, the host) and the Docker 
container:

1. Share Volumes using the `docker run` command
2. Copy files using explicit command
3. Copy files using the Dockerfile

### Share Volumes using the `docker run` command

When you run a Docker container, you can specify a shared volume between the host machine 
and the Docker container using the following command:

```bash
$ docker run --rm -it -v $PWD/app:/app IMAGE
```

Notes:

1. The `-v` option specifies a volume list:
    - The first item in the list is the shared folder name on the host machine, where the $PWD 
      refers to the folder in which the Dockerfile exists.
    - The second item in the list (after the `:`) refers to the folder name on the docker container 
      (given as absolute path).
2. Here we use a folder named `app` for both parties. However, you can use any name and they don't 
   even have to be the same names for both parties.

After entering the container, you can copy files from or to the shared folder.

### Copy Files into a Docker Container using explicit command

The following two commands provide each one direction of explicitly copying files/folders between a 
container and the local filesystem on the host machine:

```bash
$ docker cp [OPTIONS] CONTAINER:SRC_PATH DEST_PATH
$ docker cp [OPTIONS] SRC_PATH CONTAINER:DEST_PATH
```

For more details, see [`docker cp` docs][14].

### Copy Files into a Docker Container using Dockerfile

The COPY instruction in a [Dockerfile][7] copies new files or directories from <src> to the 
container at the path <dest>.

```
COPY <src> <dst>
```

For more details, see [`COPY` docs][15].

---

**Related Guides:**

- [Docker Overview][6]
- [Docker Installation][2]

---

[1]: https://docs.docker.com/
[2]: /Guides/Docker/Docker%20Installation
[3]: /Guides/Vagrant/Vagrant%20Overview
[4]: /Guides/Vagrant/Getting%20Started%20with%20Vagrant
[5]: https://docs.docker.com/engine/reference/commandline/cli/
[6]: /Guides/Docker/Docker%20Overview
[7]: /Topics/Dockerfile
[8]: https://docs.docker.com/edge/engine/reference/commandline/image_build/
[9]: https://docs.docker.com/engine/reference/commandline/create/
[10]: https://docs.docker.com/engine/reference/run/
[11]: https://hub.docker.com/_/alpine/
[12]: https://hub.docker.com/_/ubuntu/
[13]: https://hub.docker.com/
[14]: https://docs.docker.com/engine/reference/commandline/cp/
[15]: https://docs.docker.com/engine/reference/builder/#copy

