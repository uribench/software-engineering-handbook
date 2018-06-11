# Recommended SSH Clients

Recommended [SSH Clients][1]:

- [PuTTY][2] -          SSH Client and terminal emulator
- [MobaXterm][3] -      SSH Client and tabbed terminal emulator

## Tips for using PuTTY

### Auto-login 

Auto-login with a given username can be set in PuTTY as follows:

1. Load the relevant saved session for which this setting will apply
2. Go to "Connection > Data" and set the text field 'Auto-login username' 
3. Save the session 

### Creating a Shortcut to a Saved Session

To create a shortcut to PuTTY that automatically launches a given session do:

1. Create a shortcut to the PuTTY Application
2. Open the shortcut properties and modify the "Target" field: `"Path\To\PuTTY\putty.exe" -load "<saved-session-name>"`

---

[1]: /Topics/SSH%20Protocol
[2]: https://www.chiark.greenend.org.uk/~sgtatham/putty/
[3]: https://mobaxterm.mobatek.net/
