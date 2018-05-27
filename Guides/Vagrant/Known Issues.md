# Known Issues

The following sections describe solutions and workarounds to common known issues.

## Enabling Virtualization Technology

The Virtualization Technology (VTx) has to be enabled in the BIOS of the computer. 
To enable the VTx on the HP EliteBook 840G2 for instance, enter the BIOS by pressing F10 multiple 
times during restart. In the BIOS go to: (Advanced | Device Configuration), and scroll down and 
check the option of: 'Virtualization Technology (VTx)'.

## Microsoft Hyper-V Technology Clash

Oracle's VirtualBox Virtualization is hardware assisted by Intel's Virtualization Technology (VTx). 
Microsoft's Hyper-V Technology clashes with Oracle's VirtualBox, therefore it should be disabled 
where available.

You can disable Hyper-V using the following steps (if the windows feature was not disabled by the 
system administrator):

1. Go to 'Control Panel | Programs | Programs and Features | Turn Windows features on or off'
2. Uncheck Hyper-V settings, and click OK.

## Vagrant Update

If after turning on vagrant using 'vagrant up' command you get a notification saying that vagrant 
has an update, execute the following command to update vagrant (from the command window running from 
the directory containing the Vagrantfile of the target machine): 

```
[cmd]> vagrant box update
```

## VirtualBox Guest Additions

The VirtualBox Guest Additions consist of device drivers and system applications that optimize the 
guest operating system for better performance and usability by providing closer integration between 
host and guest. 

The Guest Additions are designed to be installed inside a virtual machine after the guest operating 
system has been installed. There are specific Guest Additions for each guest operating system.

It is recommended to upgrade the Guest Additions, if you get the following status after issuing the 
`vagrant up` command (the listed version numbers are for example only): 

```
 Checking for guest additions in VM...
 The guest additions on this VM do not match the installed version of
 VirtualBox! In most cases this is fine, but in rare cases it can
 prevent things such as shared folders from working properly. If you see
 shared folder errors, please make sure the guest additions within the
 virtual machine match the version of VirtualBox you have installed on
 your host and reload your VM.

 Guest Additions Version: 5.1.34
 VirtualBox Version: 5.2
```

To install the Guest Additions for Ubuntu VM from command line in the virtual machine:

```
$ sudo apt-get update
$ sudo apt-get install virtualbox-guest-dkms 
```

## Setting SSH key for the SSH Client

If the SSH Client you are using does not recognize the 'insecure_private_key' provided by Vagrant as 
a valid private key, use the workaround provided below to resolve that.

The Secure Shell ("SSH") protocol is all about security and Vagrant is prepackaged with an SSH key. 
Unfortunately, PuTTY and MobaXterm are not compatible with OpenSSH, out-of-the-box. Consequently, 
PuTTY and MobaXterm will not recognize the 'insecure_private_key' (which is in OpenSSH format) 
provided by Vagrant as a valid private key. 

A [workaround][1] is described below:

The basic idea to use 'PuTTYgen' (a free, open-source RSA and DSA key generation utility) to import 
and convert the 'insecure_private_key' into PuTTY's format (a .ppk file). 

PuTTYgen is normally installed as part of the normal [PuTTY][2] .msi package installation. There is 
no need for a separate PuTTYgen download.

To do so, perform the following steps:

### Step 1: Get Vagrant SSH Configuration

- Move inside the Vagrant Boxes folder under Windows (e.g., D:\Vagrant\xenial).
- Open a command window (in Windows: SHIFT + Right-Click and select "Open command window here") and 
run:

```
[cmd]> vagrant up
[cmd]> vagrant ssh-config
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

### Step 2: Open the PuTTYgen Utility

- Click on the "Load" button.
- Open the Identityfile that is mentioned above (it doesn't have an extension and that's fine 
  with PuTTYgen, as long as the File Dialog filter is set to "All Files (*.*)").
- Toward the bottom of the PuTTYgen dialog box, review the selected "Type of key to generate" 
  and the value in the "Number of bits in a generated key" box. They should be RSA and 2048, 
  respectfully.
- Press 'Save private key' button (use the .ppk extension).
  Notice where you save the file.
  (e.g., some_path\SSH Keys\SSH_vagrant-xenial_private_key.ppk)

### Step 3: Set your preferred SSH Client

Following are two examples of common SSH clients ([PuTTY][2] and [MobaXterm][3]).

#### Setting PuTTY

If you intend to use PuTTY as the SSH Client: 
- Open the PuTTY Application.
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

#### Setting MobaXterm 

- Open the MobaXterm application.
- Go into 'Session settings | SSH | Advanced SSH settings'.
- Check the "Use private key" check box.
- Point to the file saved above by PuTTYgen utility.
- Press 'OK' to dismiss the dialog (MobaXtermsave session settings changes automatically).

## Packages Update

If in the 'welcome message' you get a notification of "...packages can be updated", run the 
following command to update the package list and upgrade all of your system software to the latest 
version available:

```
$ sudo apt update
$ sudo apt -y upgrade
```

**apt** provides a high-level command line interface for the package management system.

Note: **apt** is a new package manager for Ubuntu that is intended to take over for **Apt-get**.
apt overcomes some design mistakes of apt-get. It is built to be more efficient, more secure, and 
more user friendly. Apt was introduced in Ubuntu 16.04 to simplify the package manager and to merge 
multiple commands into one single command.

To list pending updates:
```
$ sudo apt update
$ apt list --upgradable
```

## Ubuntu Update

If in the 'welcome message' you are informed that a "New Ubuntu release '...' available", 
run the following command to upgrade to it:

```
$ do-release-upgrade
```

---

[1]: https://github.com/Varying-Vagrant-Vagrants/VVV/wiki/Connect-to-Your-Vagrant-Virtual-Machine-with-PuTTY
[2]: https://www.chiark.greenend.org.uk/~sgtatham/putty/
[3]: https://mobaxterm.mobatek.net/
