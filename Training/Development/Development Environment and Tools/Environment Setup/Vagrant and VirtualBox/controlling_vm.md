## Controlling the Vagrant Virtual Machine

Once the Vagrant Virtual Machine has been [set up](setup.md), it is ready to be turned on and used.

This chapter describes how to control the life-cycle of the Vagrant Virtual Machine.

Note that the terms 'turning on', 'powering on', running', and 'booting' all mean the same in this 
tutorial, and are being used interchangeably. Similarly, 'turning off', 'powering off', 'stopping' 
and 'shutting down', are also being used here interchangeably.

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

- VirtualBox and Vagrant are both [installed](setup.md).
- The `vagrant up` command is executed from a command window opened inside the directory containing 
a file named ['Vagrantfile'](setup.md#vagrant-configuration-file).
- The [Virtualization Technology (VTx)](known_issues.md#enabling-virtualization-technology) is 
**enabled** in the BIOS.
- The [Microsoft's Hyper-V Technology](known_issues.md#microsofts-hyper-v-technology-
clash) is **disabled**.

##### Update Request

If you see a request to update, check the following known issues:

- [Vagrant Update](known_issues.md#vagrant-update)
- [Guest Additions Update](known_issues.md#oracles-virtualbox-guest-additions)

## Checking the Status of the Vagrant Virtual Machine

To check the status of the Vagrant Virtual Machine use the following command (from the command 
window running from the directory containing the Vagrantfile of the target machine):

```
[cmd]> vagrant status
```

### Status Output Examples

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


## Stopping the Vagrant Virtual Machine

After [finishing to use the VM and exiting the SSH](#using_vm.md), you can tun off the virtual 
machine using the following command (from the command window running from the directory containing 
the Vagrantfile of the target machine):

```
[cmd]> vagrant halt
```

---
