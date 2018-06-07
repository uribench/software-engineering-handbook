# SSH Protocol

The [SSH protocol][1] (also referred to as **Secure Shell**) is a method to secure the transmission 
of information over an insecure network. A common use of the SSH protocol is to secure remote login 
from one computer to another. It provides several alternative options for strong authentication, and 
it protects the communications security and integrity with strong encryption.

The protocol works in the **client-server model**, which means that the connection is established by 
the **SSH client** connecting to the **SSH server**. The SSH client drives the connection setup 
process and uses public key cryptography to verify the identity of the SSH server. After the setup 
phase, the SSH protocol uses strong symmetric encryption and hashing algorithms to ensure the 
privacy and integrity of the data that is exchanged between the client and server.

The following statements are worth mentioning:

- In the asymmetric encryption method, in which public/private key pair is used, the public key is 
used to encrypt data that can only be decrypted with the private key.
- The asymmetric encryption method with the permanent public/private key pair is used only for 
authentication, not for encrypting the information exchange. 
- After having the agreed session key it is used with a symmetric encryption method to secure all 
the communications. This type of encryption technology is often called "shared secret" encryption, 
or "secret key" encryption. Anyone who holds the key can encrypt and decrypt messages to anyone else 
holding the key.

See [How Does SSH Works][2] for more details on SSH session stages and their encryption technologies.

---

[1]: https://www.ssh.com/ssh/protocol/
[2]: /Topics/SSH%20Protocol/How%20Does%20SSH%20Works
