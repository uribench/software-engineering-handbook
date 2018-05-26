# Vagrant and VirtualBox

[VirtualBox][1] is a common virtualization software. It is an open source that was acquired by 
Oracle in 2010. VirtualBox is available on a number of host operating systems, including: Windows, 
Linux, and macOS. 

This document describes the use of [Vagrant][2], which is an open source wrapper around VirtualBox.
Vagrant makes it easy to create and run a Virtual Machine (VM) from the command line.

A simple workflow for using the Vagrant Virtual Machine after the initial settings looks as follows:

1. Turn on the VM
2. Connect to the VM
3. Use the VM
4. Disconnect from the VM
5. Turn off the VM

All the above steps, except of step 3 obviously, typically involve a single command each.

The steps described in this tutorial refer to **Windows** as the host operating system and **Linux**
as the guest operating system on the Virtual Machine (VM). However, with some minor modifications
these steps can be adapted to other environments.

## Table of Contents

- [Setting Up the Vagrant Virtual Machine](setup.md)
- [Running and Stopping the Vagrant Virtual Machine](controlling_vm.md)
- [Using the Vagrant Virtual Machine](using_vm.md)
- [Known Issues](known_issues.md)
- [Appendix](appendix.md)

---

[1]: https://www.virtualbox.org/
[2]: https://www.vagrantup.com/
