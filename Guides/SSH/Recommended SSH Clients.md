# Recommended SSH Clients

Recommended [SSH Clients][1]:

- [PuTTY][2] -          SSH Client and terminal emulator
- [MobaXterm][3] -      SSH Client and tabbed terminal emulator

## Tips for using PuTTY

### Auto-login 

Auto-login with a given username can be set in PuTTY as follows:

1. Launch PuTTY Application
2. Load the relevant saved session for which this setting will apply
3. Go to "Connection > Data" and set the text field 'Auto-login username' 
4. Save the session 

### Creating a Shortcut to a Saved Session

To create a shortcut to PuTTY that automatically launches a given session do:

1. Create a shortcut to the PuTTY Application
2. Open the shortcut properties and modify the "Target" field: 
`"Path\To\PuTTY\putty.exe" -load "<saved-session-name>"`  
**Example:** `"C:\Program Files\PuTTY\putty.exe" -load "Vagrant Session"`

## Tips for using MobaXterm

### Importing PuTTY Sessions 

MobaXTerm imports the sessions database of PuTTY, making them available for use from MobaXterm:

1. Launch MobaXterm Application
2. Select the 'Sessions' tab on the left
3. On the left panel select 'User sessions > PuTTY sessions > saved-putty-session-name' 

### Creating a Shortcut to a Saved Session

To create a shortcut to MobaXterm that automatically launches a given session do:

1. Launch MobaXterm Application
2. Right-click on the required session name and select 'Create a desktop shortcut'
3. Alternatively, follow the same steps for creating a shortcut to PuTTY as in the 
['Tips for using PuTTY'](#creating-a-shortcut-to-a-saved-session) and replace  
the `-load` option with `-bookmark`  
**Example:** `"C:\Program Files (x86)\Mobatek\MobaXterm\MobaXterm.exe" -bookmark "PuTTY sessions\Vagrant Session"`

---

[1]: /Topics/SSH%20Protocol
[2]: https://www.chiark.greenend.org.uk/~sgtatham/putty/
[3]: https://mobaxterm.mobatek.net/
