# Vagrant Overview

[Vagrant][1] is an open source wrapper around a Virtual Machine provider, such as 
[Oracle's VirtualBox][2], makes it easy to create and run a Virtual Machine (VM) from the command 
line.

VirtualBox is a common virtualization software. It is an open source that was acquired by Oracle 
in 2010. VirtualBox is available on a number of host operating systems, including: Windows, Linux, 
and macOS. 

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

The steps that refer to Windows command window can be adapted to use ['Git Bash'][3] command window 
instead.

---

**Related Guides:**

- [Vagrant Installation][4]
- [Getting Started with Vagrant][5]

---

[1]: https://www.vagrantup.com/
[2]: https://www.virtualbox.org/
[3]: /Topics/Git%20Bash
[4]: /Guides/Vagrant/Vagrant%20Installation
[5]: /Guides/Vagrant/Getting%20Started%20with%20Vagrant
