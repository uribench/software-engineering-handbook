# Vagrant Installation

To setup the [Vagrant][1] virtual machine you'll need to install a few pieces of software: 

- [VirtualBox][2] -     Virtualization software 
- [Vagrant][3] -        Wrapper around VirtualBox

Additional software tools may also be required, such as one of the [recommended][4] [SSH Clients][5].


## Customizing Oracle VM VirtualBox Settings

After installing VirtualBox it requires some minor modifications to the settings as follows:
    - Launch Oracle VM VirtualBox
    - Select (File | Preferences... | General)
    - Set the "Default Machine Folder:" (by default it is on Drive C and it will take at least 6 GB)
        Example location: D:\VirtualBox VMs


## Creating Directory Structure for Vagrant Boxes

Before or after installing Vagrant, but before the provisioning of the virtual machine, create a 
directory structure in Windows for the Vagrant Boxes.

It is recommended to use the following structure:

```
Drive:\                                 For instance D:\
|
|----Vagrant\                           Main location of the Vagrant Boxes
     |
     |----guest_os_name\                The guest OS for all child projects (e.g., xenial) 
     |    |
     |    |----.vagrant\                Created automatically on the first launch of vagrant
     |    |
     |    |----some_project_name\       Directory for a project using the same guest OS 
     |    |
     |    |----another_project_name\    Another project directory using the same guest OS
     |    |
     |    |----Vagrantfile              A common config. file for all projects in this directory
     |
     |----another_guest_os_name\        Optional: Another guest OS for the child projects 
          |
          |----.vagrant\                Created automatically on the first launch of vagrant
          |
          |----some_project_name\       Directory for a project using the same guest OS 
          |
          |----another_project_name\    Another project directory using the same guest OS
          |
          |----Vagrantfile              A common config. file for all projects in this directory
```


## Provisioning the Virtual Machine

Once you have VirtualBox, Vagrant, and optionally an [SSH Client][4] installed on your system, then 
you can move on to provisioning the Virtual Machine as 
described in the next section.


### Vagrant Configuration File

To create and provision the Virtual Machine you will need a [Vagrant configuration file][6] called 
**Vagrantfile**. You can use the 

If you decide to use the included Vagarantfile as-is (recommended at least for a start), then 
make sure to name the guest_os_name directory as `xenial` (or any other name that will remind you
the selected Guest OS for all the child projects).

You may also select a different guest OS if required, just make sure to do the following steps for 
consistency:

1. Modify the required guest OS in the Vagrantfile (e.g., `config.vm.box = "ubuntu/trusty64"`)
2. Modify the name of the Virtual Box in the Vagrantfile (e.g., `vb.name = "Trusty64 Box"`)
3. Set the name of the guest_os_name in the [directory structure for the Vagrant Boxes](
   #creating-directory-structure-for-vagrant-boxes) accordingly (e.g., `trusty`)

---

**Related Guides:**

- [Getting Started with Vagrant][7]

---

[1]: /Topics/Vagrant
[2]: https://www.virtualbox.org/
[3]: https://www.vagrantup.com/
[4]: /Guides/SSH/Recommended%20SSH%20Clients
[5]: /Topics/SSH%20Clients
[6]: /Topics/Vagrantfile
[7]: /Guides/Vagrant/Getting%20Started%20with%20Vagrant