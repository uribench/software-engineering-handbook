# Git Overview

[Git][1] is an open source distributed version control system originally developed by Linus Torvalds 
to support the development of the linux kernel.

Typically, every project has its own dedicated local Git repository with complete history and full 
version tracking capabilities, not dependent on network access or a central server.

A comprehensive coverage of Git is provided by the [Pro Git book][2]. The entire Pro Git book, 
written by Scott Chacon and Ben Straub and published by Apress, is available [online][2] for free.

The following summary of the main difference between Git and other Version Control Systems 
(VCS) is based on the description in the [Pro Git book][3]:

Other VCS store information as a set of files and the changes made to each file over time (this is 
commonly described as **delta-based version control**). However, Git stores its data as a series of 
compressed snapshots, not differences. With Git, every time you commit, or save the state of your 
project, Git basically takes a snapshot of what all your files look like at that moment and stores a 
reference to that snapshot. This creates a **stream of snapshots**. Each snapshot is a miniature 
file-system.

---

**Related Guides:**

- [Git Installation][4]
- [Getting Started with Git][5]
- [Working with a Remote Git Repository][6]

---

[1]: https://git-scm.com/
[2]: https://git-scm.com/book/en/v2
[3]: https://git-scm.com/book/en/v2/Getting-Started-Git-Basics
[4]: /Guides/Git/Git%20Installation
[5]: /Guides/Git/Getting%20Started%20with%20Git
[6]: /Guides/Git/Working%20with%20a%20Remote%20Git%20Repository