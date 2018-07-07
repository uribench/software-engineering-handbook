# Dockerfile

The configuration file for [Docker][1] is called **Dockerfile** (casing does not matter unless 
your file system is running in a strict case sensitive mode).

Dockerfile has a simple syntax for defining the steps needed to create the image and run it. Each 
instruction in a Dockerfile creates a **layer** in the image. When you change the Dockerfile and 
rebuild the image, only those layers which have changed are rebuilt. This is part of what makes 
images so lightweight, small, and fast, when compared to other virtualization technologies.

## Example Dockerfile

Following is an example for a Dockerfile. It is minimalist, but fully functional.

```
ToDo: Add example
```

---

[1]: https://docs.docker.com/