Vagrant and VirtualBox
======================

[VirtualBox][1] is a common virtualization software. It is an open source that was acquired by 
Oracle in 2010. VirtualBox is available on a number of host operating systems, including: Windows, 
Linux, and macOS. 

This document describes the use of [Vagrant][2], which is an open source wrapper around VirtualBox.
Vagrant makes it easy to create and run a virtual machine from the command line.

The steps described in this document refer to **Windows** as the host operating system and **Linux**
as the guest operating system on the Virtual Machine (VM). However, with some minor modifications
these steps can be adapter to other environments.

## Table of Contents

- [Dependencies](#dependencies)
- [Preparations](#preparations)
    - [Enabling Virtualization Technology](#enabling-virtualization-technology)
    - [Customizing VirtualBox Settings](#customizing-virtualbox-settings)
    - [Creating Directory Structure for Vagrant Boxes](#creating-directory-structure-for-vagrant-boxes)
- [Provisioning the Virtual Machine](#provisioning-the-virtual-machine)
    - [Vagrant Configuration File](#vagrant-configuration-file)
    - [Running the Virtual Machine](#running-the-virtual-machine)
- [Connecting with the Vagrant Virtual Machine](#connecting-with-the-Vagrant-Virtual-Machine)
    - [Using Local SSH](#using-local-ssh)
    - [Using Remote SSH](#using-remote-ssh)
        - [Setting SSH key for the SSH Client](#setting-ssh-key-for-the-ssh-client)
- [Logging into the Vagrant Virtual Machine](#logging-into-the-vagrant-virtual-machine)
- [Sharing Files between Windows and Vagrant Virtual Machine](#sharing-files-between-windows-and-vagrant-virtual-machine)
- [Logging off the Vagrant Virtual Machine](#logging-off-the-vagrant-virtual-machine)
- [Stopping the Vagrant Virtual Machine](#stopping-the-vagrant-virtual-machine)

## Dependencies

To setup the virtual machine you'll need to install a few pieces of software. 

Following is the basic list of required software:  

- [VirtualBox][1] -     Virtualization software 
- [Vagrant][2] -        Wrapper around VirtualBox

Additional software tools are optionally required:  

- [Git][3] -            Source control system
- [PuTTY][4] -          SSH Client and terminal emulator
- [MobaXterm][5] -      SSH Client and tabbed terminal emulator 

## Preparations

### Enabling Virtualization Technology

The Virtualization Technology (VTx) has to be enabled in the BIOS of the computer. 
To enable the VTx on the HP EliteBook 840G2 for instance, enter the BIOS by pressing F10 multiple 
times during restart. In the BIOS go to: (Advanced | Device Configuration), and scroll down and 
check the option of: 'Virtualization Technology (VTx)'.

### Customizing VirtualBox Settings

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

## Provisioning the Virtual Machine

Once you have VirtualBox, Vagrant, and optionally Git and an SSH terminal emulator (e.g., PuTTY, 
MobaXterm or equivalent) installed on your system, then you can move on to provisioning the Virtual 
Machine as described in the next sections.

### Vagrant Configuration File

To create and provision the Virtual Machine you'll need to download a Vagrant configuration file
called **Vagrantfile** (casing does not matter unless your file system is running in a strict case 
sensitive mode).

As described in [vagrantup.com][6]: 

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
using one of the [Ubuntu releases][7]: 16.04.4 LTS (Xenial Xerus) as the guest operating system.  

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

### Running the Virtual Machine

Start by moving inside the Vagrant Boxes directory under Windows to the directory that hosts the 
relevant Vagrantfile (e.g., D:\Vagrant\xenial).

Open a command line terminal (in Windows: SHIFT + Right-Click and select "Open command window here").
Alternatively, use 'Git Bash' command window that is bundled with the installation of [Git][3]. 

'Git Bash' sits on top of [MingW64][8]. MinGW (Minimalist GNU for Windows) is a distribution that 
contains a subset of the tools used for Linux/Unix environment that have been ported to windows. It 
includes compilers, a shell, and common command line tools.

'Git Bash' can be configured using ['.bashrc', '.bash_profile', '.profile'][9], but the default 
settings are good enough for a start.

Note: All the remaining commands in this document can be done either from 'Git Bash' command window 
or Windows command window. The 'Git Bash' command window not only feels better, but allows executing
git commands (described separately).

Now 'turn on' the virtual machine by running this command (e.g., from 'Git Bash'):
```
    $ vagrant up
```

Note: The first time the 'vagrant up' command runs it will take a bit of time as it downloads the 
operating system image, but later 'vagrant up' commands will be faster as the OS image is cached 
internally.

Once the virtual machine is running, you should see the command finish with several lines of text 
with the last one like:
```
    ...
    default: Finished provisioning, now run 'vagrant ssh' to enter the virtual machine.
```

If you see an error, go back and make sure you've enabled the [Virtualization Technology (VTx)](#
enabling-virtualization-technology) in the BIOS, and installed both VirtualBox and Vagrant. 
Also, make sure you're executing the command from inside the directory containing a file named 
'Vagrantfile'.

If after turning on vagrant using 'vagrant up' command you get a notification saying that vagrant 
has an update, execute the following command to update vagrant (from 'Git Bash' after 'vagrant up' 
command):
```
    $ vagrant box update
```

## Checking the Status of the Vagrant Virtual Machine
To check the status of the Vagrant Virtual Machine use the following command (from 'Git Bash'):
```
    $ vagrant status
```

For a running Vagrant Virtual Machine, for instance, you will get something similar to:
```
    Current machine states:

    default                   running (virtualbox)

    The VM is running. To stop this VM, you can run `vagrant halt` to
    shut it down forcefully, or you can run `vagrant suspend` to simply
    suspend the virtual machine. In either case, to restart it again,
    simply run `vagrant up`.

```

For a stopped Vagrant Virtual Machine, for instance, you will get something similar to:
```
    Current machine states:

    default                   poweroff (virtualbox)

    The VM is powered off. To restart the VM, simply run `vagrant up`

```

You can monitor the status of the Vagrant Virtual Machine also from the Oracle VM VirtualBox as 
follows:
    - Launch Oracle VM VirtualBox
    - Select the "Machine Tools" tab
    - On the left panel you will see the assigned name of the Virtual Box (e.g., Xenial64 Box)
      with the Status below it (e.g., "Powered Off", "Running")

## Connecting with the Vagrant Virtual Machine

Now that vagrant is up, you have to connect to the running Vagrant Virtual Machine.

Two alternative methods for connecting with the running Vagrant Virtual Machine are introduced in 
the next sections:

1. Using Local SSH
2. Using Remote SSH (e.g., with PuTTY or MobaXterm or similar)

### Using Local SSH

Once the virtual machine is running you can enter a Linux command terminal on it by executing the 
command (from 'Git Bash' after 'vagrant up' command):
```
    $ vagrant ssh
```
After completing the above successfully, you are now connected to the running virtual machine and 
ready to [log into it](#logging-into-the-vagrant-virtual-machine).

### Using Remote SSH

The above section described how to connect to to a running Virtual Machine using local SSH. 

However, once the virtual machine is running you can connect to it using an SSH Client instead 
(either locally or remotely), such as [PuTTY][4] or [MobaXterm][5] or similar.

Connect to the assigned port of the running Virtual Machine (default: 2222) on the respective 
hosting machine (on a local machine you can use for Host Name either 'localhost' or 127.0.0.1).

If the SSH Client you are using do not recognize the 'insecure_private_key' provided by Vagrant as a 
valid private key, use the steps in the next section to resolve that.

After completing the above successfully, you are now connected to the running virtual machine and 
ready to [log into it](#logging-into-the-vagrant-virtual-machine).

#### Setting SSH key for the SSH Client

The Secure Shell ("SSH") protocol is all about security and Vagrant is prepackaged with an SSH key. 
Unfortunately, PuTTY and MobaXterm are not compatible with OpenSSH, out-of-the-box. Consequently, 
PuTTY and MobaXterm will not recognize the 'insecure_private_key' (which is in OpenSSH format) 
provided by Vagrant as a valid private key. 

A [workaround][9] is described below:

The basic idea to use 'PuTTYgen' (a free, open-source RSA and DSA key generation utility) to import 
and convert the 'insecure_private_key' into PuTTY's format (a .ppk file). 

PuTTYgen is normally installed as part of the normal [PuTTY][4] .msi package installation. There is 
no need for a separate PuTTYgen download.

To do so, perform the following steps:

1. Get Vagrant SSH Configuration:
    - Move inside the Vagrant Boxes folder under Windows (e.g., D:\Vagrant\xenial).
    - Open a 'Git Bash' command window and run:
```
    $ vagrant up
    $ vagrant ssh-config
        Output:
            Host default
              HostName 127.0.0.1
              User vagrant
              Port 2222
              UserKnownHostsFile /dev/null
              StrictHostKeyChecking no
              PasswordAuthentication no
              IdentityFile D:/Vagrant/xenial/.vagrant/machines/default/virtualbox/private_key
              IdentitiesOnly yes
              LogLevel FATAL
```
2. Open the PuTTYgen utility:
    - Click on the Load button;
    - Open the Identityfile that is mentioned above (it doesn't have an extension and that's fine 
      with PuTTYgen as long as the File Dialog filter is set to "All Files (*.*)").
    - Toward the bottom of the PuTTYgen dialog box, review the selected "Type of key to generate" 
      and the value in the "Number of bits in a generated key" box. They should be RSA and 2048, 
      respectfully.
    - Press 'Save private key' button (use the .ppk extension).
      Notice where you save the file.
      (e.g., some_path\SSH Keys\SSH_vagrant-xenial_private_key.ppk)
3. If you intend to use PuTTY as the SSH Client: Open the PuTTY application:
    - Using the 'Session' tab set:
```
        Hostname: localhost
        Port: 2222
```
    - Using the 'Connection | SSH | Auth' tab set:
```
        Private key file for authentication: (point to the file saved above by PuTTYgen utility)
```
    - Go back to the 'Session' tab and save the session with a preferred name (e.g., `vagrant`)
4. If you intend to use MobaXterm as the SSH Client: Open the MobaXterm application:
    - Go into 'Session settings | SSH | Advanced SSH settings'.
    - Check the "Use private key" check box.
    - Point to the file saved above by PuTTYgen utility.
    - Press 'OK' to dismiss the dialog (MobaXtermsave session settings changes automatically).

## Logging into the Vagrant Virtual Machine

After using any of the above two methods to connect with the running Vagrant Virtual Machine, you 
are ready to logging into it.

You will be asked for password with something like:
    vagrant@127.0.0.1's password:

Enter the default password for vagrant user name: `vagrant`

You should get a 'welcome message' that looks something like:
```
    Welcome to Ubuntu 16.04.4 LTS (GNU/Linux 4.4.0-127-generic x86_64)
    ... more lines
```

Followed by an Ubuntu Linux command prompt that looks something like:
```
    vagrant@ubuntu-xenial:~$ 
```

If in the 'welcome message' you get a notification of "...packages can be updated", you can perform
the update using the following command:
```
    $ sudo apt update
```
**apt** provides a high-level command line interface for the package management system.

If in the 'welcome message' you are informed that a "New Ubuntu release '...' available", 
run the following command to upgrade to it:
```
    $ do-release-upgrade
```

After completing the above, you are now connected to the running virtual machine and ready to use it.

## Sharing Files between Windows and Vagrant Virtual Machine

More TBD

## Logging off the Vagrant Virtual Machine

When you are done using the virtual machine, you can log off and exit the SSH using:
```
    $ exit (or Ctrl-D)
```

## Stopping the Vagrant Virtual Machine

After exiting the SSH, you can tun off the virtual machine using the following command (from 
'Git Bash' running from the directory containing the Vagrantfile of the target machine):
```
    $ vagrant halt
```


---

[1]: https://www.virtualbox.org/
[2]: https://www.vagrantup.com/
[3]: https://git-scm.com/
[4]: https://www.chiark.greenend.org.uk/~sgtatham/putty/
[5]: https://mobaxterm.mobatek.net/
[6]: https://www.vagrantup.com/docs/vagrantfile/
[7]: http://releases.ubuntu.com/
[8]: http://www.mingw.org/
[9]: https://superuser.com/questions/405342/mingw-bash-profile
[10]: https://github.com/Varying-Vagrant-Vagrants/VVV/wiki/Connect-to-Your-Vagrant-Virtual-Machine-with-PuTTY