# Vagrantfile

The configuration file for [Vagrant][1] is called **Vagrantfile** (casing does not matter unless your 
file system is running in a strict case sensitive mode).

As described in [vagrantup.com][2]: 

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


## Example Vegrantfile

Following is an example for a Vagrantfile. It is minimalist, but fully functional.

```
# -*- mode: ruby -*-
# vi: set ft=ruby :

# The most common configuration options are documented and commented below.
# For a complete reference, please see the online documentation at
# https://docs.vagrantup.com.
Vagrant.configure(2) do |config|
  forward_port = ->(guest, host = guest) do
    config.vm.network :forwarded_port,
      guest: guest, host: host,
      auto_correct: true
  end
  
  config.vm.box = "ubuntu/xenial64"

  config.vm.provider "virtualbox" do |vb|
    vb.name = "Xenial64 Box"
    vb.memory = "2048"
  end

  forward_port[80]        # nginx/apache
  forward_port[3000]      # generic web dev

  config.vm.synced_folder "./", "/vagrant", nfs: true
end
```

Several definitions in the above Vagrantfile example that are worth mentioning are described in the following sections.


### Required OS for the Virtual Box

The `config.vm.box = "ubuntu/xenial64"` definition specifies the required guest OS.  
This example is using one of the [Ubuntu releases][3]: 16.04.4 LTS (Xenial Xerus) as the guest 
operating system.


### Name of the Virtual Box


In the above example, only one **Virtual Machine provider** is defined (e.g., "virtualbox").
The `vb.name = "Xenial64 Box"` definition specifies the name of the Virtual Box.


### Synced Folder between Host and Guest Machines

The `config.vm.synced_folder "./", "/vagrant", nfs: true` definition specifies the two folders to be 
synced between the host (e.g., Windows) and the guest (e.g., Ubuntu).

The `config.vm.sync_folder` gets two parameters: The first parameter is a path to a directory on the 
host machine. If the path is relative, it is relative to the project root (where the respective 
Vagrantfile is located). The second parameter must be an absolute path of where to share the folder 
within the guest machine. This folder will be created (recursively, if it must) if it does not exist.

Syncing between these two folders allow you to continue working on your project's files on your host 
machine, for instance using your favorite text editor on Windows, but use the resources in the guest 
machine to compile or run your project.

In the above example, Vagrant will share your project directory (the directory with the Vagrantfile) 
to `/vagrant` on the guest VM.

---

[1]: https://www.vagrantup.com/
[2]: https://www.vagrantup.com/docs/vagrantfile/
[3]: http://releases.ubuntu.com/
