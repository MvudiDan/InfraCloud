from netmiko import ConnectHandler
from openpyxl import Workbook
import datetime

# Output Excel file
inventory_filename = 'netmiko_output.xlsx'

# Create new workbook and sheet
wb = Workbook()
ws = wb.active
ws.title = "Router Info"

# Write headers
ws.append(["Date & Time", "Hostname", "IOS Version", "System Uptime", "Number of Interfaces"])

# Get current date and time
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Connect to router
sshCli = ConnectHandler(
    device_type="cisco_ios",
    host="192.168.56.102",
    port=22,
    username="cisco",
    password="cisco123!"
)

# Get output
output = sshCli.send_command("show version")

# Parse values
ios_version = ""
hostname = ""
sys_uptime = ""
num_interfaces = ""

for line in output.splitlines():
    if "Cisco IOS Software" in line:
        ios_version = line.strip()
    elif "uptime is" in line:
        hostname = line.split()[0]
        sys_uptime = " ".join(line.split()[2:])
    elif "interface" in line.lower():
        num_interfaces = line.strip().split()[0]

sshCli.disconnect()

# Add data to Excel sheet
ws.append([now, hostname, ios_version, sys_uptime, num_interfaces])

# Save the workbook
wb.save(inventory_filename)

print(f"✅ Data saved to {inventory_filename} at {now}")
