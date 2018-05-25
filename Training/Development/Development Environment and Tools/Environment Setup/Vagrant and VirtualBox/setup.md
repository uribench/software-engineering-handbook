## Setting Up the Vagrant Virtual Machine

To setup the virtual machine you'll need to install a few pieces of software. 

Following is the basic list of required software:  

- [VirtualBox][1] -     Virtualization software 
- [Vagrant][2] -        Wrapper around VirtualBox

Additional software tools that are optionally required:  

- [PuTTY][3] -          SSH Client and terminal emulator
- [MobaXterm][4] -      SSH Client and tabbed terminal emulator 

### Customizing Oracle VM VirtualBox Settings

After installing VirtualBox it requires some minor modifications to the settings as follows:
    - Launch Oracle VM VirtualBox
    - Select (File | Preferences... | General)
    - Set the "Default Machine Folder:" (by default it is on Drive C and it will take at least 6 GB)
        Example location: D:\VirtualBox VMs

### Creating Directory Structure for Vagrant Boxes

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

### Provisioning the Virtual Machine

Once you have VirtualBox, Vagrant, and optionally an SSH terminal emulator (e.g., PuTTY, MobaXterm 
or equivalent) installed on your system, then you can move on to provisioning the Virtual Machine as 
described in the next section.

#### Vagrant Configuration File

To create and provision the Virtual Machine you'll need to download a Vagrant configuration file
called **Vagrantfile** (casing does not matter unless your file system is running in a strict case 
sensitive mode).

As described in [vagrantup.com][5]: 

> The primary function of the Vagrantfile is to describe the type of Virtual Machine required for a 
> project, and how to configure and provision this machine.
> 
> Vagrant is meant to run with one Vagrantfile per project, and the Vagrantfile is supposed to be 
> committed to version control. This allows other developers involved in the project to check out 
> the code, run vagrant up, and be on their way. Vagrantfiles are portable across every platform 
> Vagrant supports.
>
> The syntax of Vagrantfiles is **Ruby**, but knowledge of the Ruby programming language is not 
> necessary to make modifications to the Vagrantfile, since it is mostly simple variable assignment.

You can use the included [Vagrantfile](Vagrantfile). It is minimalist, but fully functional. It is 
using one of the [Ubuntu releases][6]: 16.04.4 LTS (Xenial Xerus) as the guest operating system.  

Several definitions in the included Vagrantfile that are worth mentioning here are:

- The required guest OS: `config.vm.box = "ubuntu/xenial64"`  
- The name of the Virtual Box: `vb.name = "Xenial64 Box"`

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

[1]: https://www.virtualbox.org/
[2]: https://www.vagrantup.com/
[3]: https://www.chiark.greenend.org.uk/~sgtatham/putty/
[4]: https://mobaxterm.mobatek.net/
[5]: https://www.vagrantup.com/docs/vagrantfile/
[6]: http://releases.ubuntu.com/
