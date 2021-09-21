import os
from time import sleep
from rich.console import Console
from rich.color import Color
from rich.prompt import Prompt
from rich import pretty

import json

console = Console()
#console.print()


def assign_IP_Address():
	#Assign IP address
	ip = input("Enter new ip address for add: ")
	intf_name = Prompt.ask("Enter interface name : ")
	cmd = f"sudo ip address add {ip} dev {intf_name}"
	res = os.popen(cmd).read()
	console.print(res)
	console.print("Added successfully")
	
	
def delete_IP_Address():
	#Delete IP address
	ip = input("Enter ip address for delete: ")
	intf_name = Prompt.ask("Enter interface name : ")
	cmd = f"sudo ip address delete {ip} dev {intf_name}"
	res = os.popen(cmd).read()
	console.print(res)
	console.print("deleted successfully")
	
	
def display_IP_Address():
	#Display IP address
	cmd = f"ip -c -br address"
	res = os.popen(cmd).read()
	console.print(res)
	
def display_all_interfaces():
	#Display all interfaces
	cmd = f"ip l"
	res = os.popen(cmd).read()
	console.print(res)
	
	
def configure_routing():
	#Configure routing
	nwadd = input("Enter network ip address: ")
	gtwayadd = input("Enter gateway ip address: ")
	cmd = f"ip r add {nwadd} via {gtwayadd}"
	res = os.popen(cmd).read()
	console.print(res)
	console.print("configuration completed successfully")
	
	
def turn_On_Off_interface():
	#Turn On/Off interface
	console.print("1.turn on", style="bold green")
	console.print("2.turn off", style="bold green")
	console.print("3.exit", style="bold red")
	
	while True:
		ch = int(input("Enter choice: "))
		#intf_name = Prompt.ask("Enter interface name : ")
		if ch == 1:
			#console.print("r")
		
			intf_name = Prompt.ask("Enter interface name : ")
			cmd = f"sudo ip link set dev {intf_name} up"
			res = os.popen(cmd).read()
			console.print(res)
	
		elif ch == 2:
			intf_name = Prompt.ask("Enter interface name : ")
			cmd = f"sudo ip link set dev {intf_name} down"
			res = os.popen(cmd).read()
			console.print(res)
		elif ch == 3:
			break;
		else:
			console.print("Enter correct option ")
	
	
def add_ARP_entry():
	#Add ARP entry
	ip = input("Enter new ip address for add: ")
	mac_add = input("Enter mac address for add: ")
	intf_name = Prompt.ask("Enter interface name : ")
	#cmd = f"ip l"
	arp = os.popen("ip n show").read()
	#cmd1 = f"sudo ip n add {ip} lladdr {mac_add} dev {intf_name} nud reachable"
	cmd1 = f"sudo ip n add {ip} lladdr {mac_add} dev {intf_name} nud permanent"
	res = os.popen(cmd1).read()
	console.print(arp)
	console.print("ARP Entry successfull")
	
	
def delete_ARP_Entry():
	#Delete ARP Entry
	ip = input("Enter ip address which u want to del: ")
	intf_name = Prompt.ask("Enter interface name : ")
	#cmd = f"ip l"
	#cmd = "ip n show"
	cmd = f"sudo ip n del {ip} dev {intf_name}"
	res = os.popen(cmd).read()
	#console.print(res)
	console.print("ARP Entry deleted successfully")
	
def restart_Network():
	#Restart Network
	cmd = f"sudo systemctl restart networking"
	cmd1 = f"sudo systemctl status networking"
	res = os.popen(cmd).read()
	console.print(res)
	console.print("restarted")
	re = os.popen(cmd1).read()
	#console.print(re)
	
def change_hostname():
	#Change hostname
	hostname = input("Enter new host name for change: ")
	cmd = f"hostnamectl set-hostname {hostname}"
	res = os.popen(cmd).read()
	console.print(res)
	#hostname for checking changed name
	
	
def add_DNS_server_entry():
	#Add DNS server entry
	#nameserver 8.8.8.8 format
	#ctrl+d or exit() for exit
	cmd = f"sudo cat >> /etc/resolv.conf"
	res = os.popen(cmd).read()
	console.print(res)
	console.print("Added successfully")
	
	
