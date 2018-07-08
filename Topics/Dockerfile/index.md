# Dockerfile

The configuration file for [Docker][1] is called **Dockerfile** (casing does not matter unless 
your file system is running in a strict case sensitive mode).

Dockerfile has a simple syntax for defining the steps needed to create the image and run it. Each 
instruction in a Dockerfile creates a **layer** in the image. When you change the Dockerfile and 
rebuild the image, only those layers which have changed are rebuilt. This is part of what makes 
images so lightweight, small, and fast, when compared to other virtualization technologies.

## Example Dockerfile

Following is an example for a simple Dockerfile. It is minimalist, but fully functional.

```
FROM alpine

WORKDIR /app

# RUN apt install

COPY ./app .

CMD sh
```

In simple words, the above Dockerfile instructs docker to use 'Alpine Linux' when building a Docker 
image. 

It also defines the working directory as `/app` in order to enter it immediately after running a 
Docker container that is created from this Docker image.

It install dependencies (here the `apt` dependency is commented out)

This Dockerfile instructs to copy the content of the current directory of the hosting Linux VM into 
the Linux working directory of the container. 

Note that with this simple `COPY` command, it will happen as part of the process of Docker container 
creation. Meaning, only during the `docker build`, and not during the `docker run`.

Finally, the above Dockerfile instructs to run the `sh` simple terminal in the Docker container when 
it will run.

See the official documentation of the [Dockerfile format][2] for more details.

---

[1]: https://docs.docker.com/
[2]: https://docs.docker.com/engine/reference/builder/#format