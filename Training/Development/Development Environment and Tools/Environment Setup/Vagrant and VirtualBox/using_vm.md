## Using the Vagrant Virtual Machine

The Vagrant Virtual Machine (VM) can be used after [bringing it up successfully](controlling_vm.md).

The following sections describe how to perform a typical usage workflow:

- [Connect](#connecting-with-the-vagrant-virtual-machine) with a running Vagrant VM, 
- [Log in](#logging-into-the-vagrant-virtual-machine) into it,
- [Share files](#sharing-files-between-windows-and-vagrant-virtual-machine) between the host and 
guest operating systems, 
- and finally [log off](#logging-off-the-vagrant-virtual-machine) the VM.

## Connecting with the Vagrant Virtual Machine

Now that vagrant is up, you have to connect to the running Vagrant Virtual Machine.

Two alternative methods for connecting with the running Vagrant Virtual Machine are introduced in 
the next sections:

1. Using Local SSH
2. Using Remote SSH (e.g., with PuTTY or MobaXterm or similar)

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

However, once the virtual machine is running you can connect to it using an SSH Client instead 
(either locally or remotely), such as [PuTTY][1] or [MobaXterm][2] or similar.

Connect to the assigned port of the running Virtual Machine (default: 2222) on the respective 
hosting machine (on a local machine you can use for Host Name either 'localhost' or 127.0.0.1).

If the SSH Client you are using does not recognize the 'insecure_private_key' provided by Vagrant as 
a valid private key, use the [workaround](known_issues.md#setting-ssh-key-for-the-ssh-client) to 
resolve that.

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
to [upgrade](known_issues.md#packages-update) all of your packages to the latest version available.

If in the 'welcome message' you are informed that a "New Ubuntu release '...' available", you may 
want to [upgrade](known_issues.md#ubuntu-update) it to the latest version available.

After completing the above, you are now connected to the running virtual machine and ready to use it.

## Sharing Files between Windows and Vagrant Virtual Machine

The `config.vm.synced_folder` definition in the [Vagrantfile](setup.md#vagrant-configuration-file) 
specifies the two folders to be synced between the host (e.g., Windows) and the guest (e.g., Ubuntu).

The `sync_folder` gets two parameters: The first parameter is a path to a directory on the host 
machine. If the path is relative, it is relative to the project root (where the respective 
Vagrantfile is located). The second parameter must be an absolute path of where to share the folder 
within the guest machine. This folder will be created (recursively, if it must) if it does not exist.

Syncing between these two folders allow you to continue working on your project's files on your host 
machine, for instance using your favorite text editor on Windows, but use the resources in the guest 
machine to compile or run your project.

In the attached [Vagrantfile](Vagrantfile) the following definition, which is the default, is used:

```
config.vm.synced_folder "./", "/vagrant", nfs: true
```

This means that Vagrant will share your project directory (the directory with the Vagrantfile) to 
`/vagrant` on the guest VM.

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

[1]: https://www.chiark.greenend.org.uk/~sgtatham/putty/
[2]: https://mobaxterm.mobatek.net/
