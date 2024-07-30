import subprocess
import platform

def get_wifi_passwords():
    """
    Detects the operating system and calls the appropriate function to retrieve Wi-Fi passwords.
    """
    os_type = platform.system()

    if os_type == "Windows":
        return get_wifi_passwords_windows()
    elif os_type == "Linux":
        return get_wifi_passwords_linux()
    elif os_type == "Darwin":
        return get_wifi_passwords_mac()
    else:
        print("Unsupported OS")
        return []

def get_wifi_passwords_windows():
    """
    Retrieves Wi-Fi profiles and passwords on Windows using netsh commands.
    """
    try:
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

        wifi_passwords = []
        for profile in profiles:
            try:
                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
                results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                wifi_passwords.append((profile, results[0] if results else ""))
            except subprocess.CalledProcessError:
                wifi_passwords.append((profile, "ENCODING ERROR"))
        return wifi_passwords
    except Exception as e:
        print(f"Error: {e}")
        return []

def get_wifi_passwords_linux():
    """
    Retrieves Wi-Fi profiles and passwords on Linux using nmcli commands.
    Requires sudo permissions to access passwords.
    """
    try:
        data = subprocess.check_output(['nmcli', '-t', '-f', 'NAME', 'connection', 'show']).decode('utf-8').split('\n')
        profiles = [line for line in data if line]

        wifi_passwords = []
        for profile in profiles:
            try:
                result = subprocess.check_output(['sudo', 'nmcli', '-s', '-g', '802-11-wireless-security.psk', 'connection', 'show', profile]).decode('utf-8').strip()
                wifi_passwords.append((profile, result))
            except subprocess.CalledProcessError:
                wifi_passwords.append((profile, "No password or encoding error"))
        return wifi_passwords
    except Exception as e:
        print(f"Error: {e}")
        return []

def get_wifi_passwords_mac():
    """
    Retrieves Wi-Fi profiles and passwords on macOS using networksetup and security commands.
    """
    try:
        data = subprocess.check_output(["/usr/sbin/networksetup", "-listallhardwareports"]).decode('utf-8').split('\n')
        wifi_passwords = []
        for i in range(len(data)):
            if "Wi-Fi" in data[i] or "AirPort" in data[i]:
                wifi_index = i + 1
                break
        else:
            print("No Wi-Fi interface found")
            return []
        
        interface = data[wifi_index].split(": ")[1]
        profiles = subprocess.check_output(["/usr/sbin/networksetup", "-listpreferredwirelessnetworks", interface]).decode('utf-8').split('\n')[1:]

        for profile in profiles:
            try:
                profile = profile.strip()
                result = subprocess.check_output(["/usr/bin/security", "find-generic-password", "-wa", profile], stderr=subprocess.DEVNULL).decode('utf-8').strip()
                wifi_passwords.append((profile, result))
            except subprocess.CalledProcessError:
                wifi_passwords.append((profile, "No password or encoding error"))
        return wifi_passwords
    except Exception as e:
        print(f"Error: {e}")
        return []

def display_wifi_passwords(wifi_passwords):
    """
    Displays the Wi-Fi profiles and their associated passwords in a formatted manner.
    """
    for profile, password in wifi_passwords:
        print(f"{profile:<30}|  {password}")

if __name__ == "__main__":
    wifi_passwords = get_wifi_passwords()
    display_wifi_passwords(wifi_passwords)
