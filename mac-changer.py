import subprocess
import time

mac = input("[+] Enter your desired MAC address: ")

interface = "eth0"

print(f"[+] Changing MAC address for {interface} to {mac}")

subprocess.call("sudo ip link set dev " + interface + " down", shell=True)
time.sleep(2)

subprocess.call("sudo ip addr flush dev " + interface, shell=True)

subprocess.call("sudo ip link set dev " + interface + " address " + mac, shell=True)

subprocess.call("sudo ip link set dev " + interface + " up", shell=True)

subprocess.call("ip link show " + interface, shell=True)

