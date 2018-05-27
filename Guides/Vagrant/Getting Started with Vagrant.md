# Getting Started with Vagrant

Once the [Vagrant][1] Virtual Machine has been [installed][2], it is ready to be turned on and used.

Two main subjects are covered in the following sections:

- [Vagrant Life Cycle Management](#Vagrant Life Cycle Management)
- [Basic Use of the Vagrant Virtual Machine](#Basic Use of the Vagrant Virtual Machine)

## Vagrant Life Cycle Management

To control the life-cycle of the Vagrant Virtual Machine you will need to know two basic commands:

- How to run the Virtual Machine: `vagrant up`
- How to stop the Virtual Machine: `vagrant halt`

It is helpful also to know how to monitor the status of the Virtual Machine: `vagrant status`

Note that the terms 'turning on', 'powering on', running', and 'booting' all mean the same in this 
tutorial, and are being used interchangeably. Similarly, 'turning off', 'powering off', 'stopping' 
and 'shutting down', are also being used here interchangeably.

The remaining of this document explains the above commands in details, and provides help with common
known issues.

### Running the Virtual Machine

Start by moving inside the Vagrant Boxes directory under Windows to the directory that hosts the 
relevant Vagrantfile (e.g., D:\Vagrant\xenial).

Open a command window (in Windows: SHIFT + Right-Click and select "Open command window here").

Now 'turn on' the virtual machine by running this command from the command window:

```
[cmd]> vagrant up
```

Note: The first time the 'vagrant up' command runs it will take a bit of time as it downloads the 
operating system image, but later 'vagrant up' commands will be faster as the OS image is cached 
internally.

Once the virtual machine is running, you should see the command finish with several lines of text 
with the last one like:

```
default: Finished provisioning, now run 'vagrant ssh' to enter the virtual machine.
```

#### Potential Issues with `vagrant up` Command

While the system processes the `vagrant up` command it is supposed to display progress status lines
starting with something similar to the following:

```
Bringing machine 'default' up with 'virtualbox' provider...
```

Observe the status lines carefully for potential issues (e.g., errors, request for update).

##### Errors
If you see an error, check the following known issues:

- VirtualBox and Vagrant are both [installed][2].
- The `vagrant up` command is executed from a command window opened inside the directory containing 
a file named 'Vagrantfile'.
- The [Virtualization Technology (VTx)][4] is **enabled** in the BIOS.
- The [Microsoft's Hyper-V Technology][5] is **disabled**.

##### Update Request

If you see a request to update, check the following known issues:

- [Vagrant Update][6]
- [Guest Additions Update][7]

### Checking the Status of the Vagrant Virtual Machine

To check the status of the Vagrant Virtual Machine use the following command (from the command 
window running from the directory containing the Vagrantfile of the target machine):

```
[cmd]> vagrant status
```

#### Status Output Examples

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


### Stopping the Vagrant Virtual Machine

After [finishing to use the VM and exiting the SSH](#using_vm.md), you can tun off the virtual 
machine using the following command (from the command window running from the directory containing 
the Vagrantfile of the target machine):

```
[cmd]> vagrant halt
```

## Basic Use of the Vagrant Virtual Machine

The Vagrant Virtual Machine (VM) can be used after [bringing it up successfully](#running-the-
virtual-machine).

The following sections describe a typical usage workflow:

- [Connect](#connecting-with-the-vagrant-virtual-machine) to a running Vagrant VM, 
- [Log in](#logging-into-the-vagrant-virtual-machine) into it,
- [Share files](#sharing-files-between-windows-and-vagrant-virtual-machine) between the host and 
guest operating systems, 
- and finally [log off](#logging-off-the-vagrant-virtual-machine) the VM.

### Connecting with the Vagrant Virtual Machine

Now that vagrant is up, you have to connect to the running Vagrant Virtual Machine.

Two alternative methods for connecting with the running Vagrant Virtual Machine are introduced in 
the next sections:

1. Using Local SSH
2. Using Remote SSH

### Using Local SSH

Once the virtual machine is running you can enter a Linux command terminal on it by executing the 
command (from the command window running from the directory containing the Vagrantfile of the target 
machine):

```
[cmd]> vagrant ssh
```

After completing the above successfully, you are now connected to the running virtual machine and 
ready to [log into it](#logging-into-the-vagrant-virtual-machine).

### Using Remote SSH

The above section described how to connect to a running Virtual Machine using local SSH. 

However, once the virtual machine is running you can connect to it using an [SSH Client][8] instead 
(either locally or remotely), such as any of the [recommended SSH Clients][9] or similar.

Connect to the assigned port of the running Virtual Machine (default: 2222) on the respective 
hosting machine (on a local machine you can use for Host Name either 'localhost' or 127.0.0.1).

If the SSH Client you are using does not recognize the 'insecure_private_key' provided by Vagrant as 
a valid private key, use the [workaround][10] to resolve that.

After completing the above successfully, you are now connected to the running virtual machine and 
ready to [log into it](#logging-into-the-vagrant-virtual-machine).

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

If in the 'welcome message' you get a notification of "...packages can be updated", you may want to
to [upgrade](#known_issues.md#packages-update) all of your packages to the latest version available.

If in the 'welcome message' you are informed that a "New Ubuntu release '...' available", you may 
want to [upgrade](#known_issues.md#ubuntu-update) it to the latest version available.

After completing the above, you are now connected to the running virtual machine and ready to use it.

## Sharing Files between Windows and Vagrant Virtual Machine

The `config.vm.synced_folder` definition in the [Vagrantfile][11] specifies the two folders to be 
synced between the host (e.g., Windows) and the guest (e.g., Ubuntu).

Syncing between these two folders allow you to continue working on your project's files on your host 
machine, for instance using your favorite text editor on Windows, but use the resources in the guest 
machine to compile or run your project.

Note that after issuing the `vagrant up` command with the above definition, the following lines 
are displayed:

```
Mounting shared folders...
/vagrant => D:/Vagrant/xenial
```

## Logging off the Vagrant Virtual Machine

When you are done using the virtual machine, you can log off and exit the SSH using:

```
$ exit (or Ctrl-D)
```

---

[1]: Topics/Vagrant
[2]: Guides/Vagrant/Vagrant%20Installation
[3]: Topics/SSH%20Clients
[4]: Guides/Vagrant/Known%20Issues#Enabling%20Virtualization%20Technology
[5]: Guides/Vagrant/Known%20Issues#Microsofts%20Hyper-v%20Technology%20Clash
[6]: Guides/Vagrant/Known%20Issues#Vagrant%20Update
[7]: Guides/Vagrant/Known%20Issues#VirtualBox%20Guest%20Additions
[8]: Topics/SSH%20Clients.md
[9]: Guides/SSH/Recommended%20SSH%20Clients.md
[10]: Guides/Vagrant/Known%20Issues#Setting%20SSH%20key%20for%20the%20SSH%20Client
[11]: Topics/Vagrantfile
