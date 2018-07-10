# Generating an SSH Key Pair

The [SSH protocol][1] employs public key cryptography for authentication using public and private 
SSH key pair with an asymmetric encryption method. The authentication keys, called SSH keys, are 
created using the [`ssh-keygen`][2] tool which is available for multiple operating system.

## Types of SSH Keys

`ssh-keygen` is able to generate several types of SSH keys using different digital signature 
algorithms (i.e., `dsa`, `ecdsa`, `ed25519`, or `rsa`).

## SSH Keys Passphrase

The generated SSH keys are stored locally on your system. To add an extra layer of security, you can 
decide to protect the private key with a [passphrase][2]. This way, the passphrase has to be 
provided in order to gain access to the private key. The passphrase can be assigned when new SSH keys 
are generated, or later to an existing SSH keys. The passphrase can be modified later at any time. 
The passphrase is created and managed using the `ssh-keygen` tool.

## Usage

The `ssh-keygen` command [syntax][3] is:

```bash
$ ssh-keygen [options]
```

For instance, [GitHub instructions][4] for generating SSH keys to be used for authentication with 
their server are as follows:

```bash
$ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

The options used in the above command are:

- `-t` specifies the desired digital signature algorithm (e.g., `rsa`)
- `-b` specifies the number of bits in the key
- `-C` specifies the comment/label to be associated with the keys

---

[1]: /Topics/SSH%20Protocol
[2]: https://www.ssh.com/ssh/passphrase
[3]: https://man.openbsd.org/ssh-keygen
[4]: https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/