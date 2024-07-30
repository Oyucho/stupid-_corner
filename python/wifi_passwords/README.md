## Wifi Password
A script that works across Windows, Ubuntu, and macOS to retrieve saved Wi-Fi profiles and passwords involves checking the operating system and using appropriate commands for each platform.

In the  script:

1. Windows: It uses netsh commands to access Wi-Fi profiles and passwords.

2. macOS: It uses the following commands:

networksetup: This command-line tool manages network settings, including listing preferred wireless networks.
security: This tool is used to access the macOS keychain, where Wi-Fi passwords are stored.

3. Linux (Ubuntu): It uses nmcli:

nmcli (Network Manager Command Line Interface): This tool is used to manage network connections and retrieve network-related information, including Wi-Fi passwords.

## How to Run the Script
1. Ensure Python is Installed:

Make sure you have Python installed on your system. You can check by running python --version or python3 --version in your terminal or command prompt.

2. Permissions and Requirements:

Windows: No additional permissions are required.

Linux: The script requires nmcli, which is part of the NetworkManager package. If it's not installed, you can install it using your package manager (e.g., sudo apt-get install network-manager).

macOS: The script uses built-in utilities (networksetup and security), and no additional setup is required.

3. Run the Script:

Windows: Open Command Prompt and run:
python wifipassword.py

Linux: Open a terminal and run with sudo permissions:
sudo python wifipassword.py
or
sudo python3 wifipassword.py

macOS: Open Terminal and run:
python wifipassword.py
or
python3 wifipassword.py

4. View the Output:

The script will output the list of Wi-Fi profiles and their associated passwords (if available) in a formatted manner.

## Important Notes
1. Permissions: On Linux and macOS, you may need administrative privileges to access stored Wi-Fi passwords.

2. Security: The script accesses sensitive information. Ensure it is used responsibly and that your system's security and privacy settings allow for this kind of operation.

3. Compatibility: The script is designed to work on Windows, Linux, and macOS. However, it may need adjustments for different Linux distributions or if certain command-line tools are missing or behave differently.

4. Error Handling: The script includes basic error handling to manage exceptions and unsupported systems.