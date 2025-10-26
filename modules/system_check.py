import platform
import subprocess

def run():
    data = {}
    data["os"] = platform.system()
    data["version"] = platform.version()
    
    # Example: Check if firewall is active (Windows)
    if data["os"] == "Windows":
        try:
            result = subprocess.check_output("netsh advfirewall show allprofiles", shell=True).decode()
            data["firewall_active"] = "ON" in result
        except:
            data["firewall_active"] = False
    else:
        data["firewall_active"] = None

    # Check for pending updates (simplified)
    data["updates_pending"] = "Check manually"  # Future: automate per OS

    return data
