import os
from time import sleep
from rich.console import Console
from rich.color import Color
from rich.prompt import Prompt
from rich import pretty
import json
from nmtool import *

console = Console()
console.print()

def main():
	console.print("1.Assign IP address", style="bold green")
	console.print("2.Delete IP address", style="bold green")
	console.print("3.Display IP address", style="bold green")
	console.print("4.Display all interfaces", style="bold green")
	console.print("5.Configure routing", style="bold green")
	console.print("6.Turn On/Off interface", style="bold green")
	console.print("7.Add ARP entry", style="bold green")
	console.print("8.Delete ARP Entry", style="bold green")
	console.print("9.Restart Network", style="bold green")	
	console.print("10.Change hostname", style="bold green")
	console.print("11.Add DNS server entry", style="bold green")
	console.print("12.Exit", style="bold red")
	
while True:
	main()
	ch =  int(input("Enter choice: "))
	
	
	if ch == 1:
		#Assign IP address
		assign_IP_Address()
	elif ch == 2:
		#Delete IP address
		delete_IP_Address()
		
	elif ch == 3:
		#Display IP address
		display_IP_Address()
		
	elif ch == 4:
		#Display all interfaces
		display_all_interfaces()
	elif ch == 5:
		#Configure routing
		configure_routing()
		
	elif ch == 6:
		#Turn On/Off interface
		turn_On_Off_interface()
	
	elif ch == 7:
		#Add ARP entry
		add_ARP_entry()
		
	elif ch == 8:
		#Delete ARP Entry
		delete_ARP_Entry()
		
	elif ch == 9:
		#Restart Network
		restart_Network()
		
	elif ch == 10:
		#Change hostname
		change_hostname()
		
	elif ch == 11:
		#Add DNS server entry
		add_DNS_server_entry()
		
	elif ch == 12:
		break;
	else:
		print("Wrong Choice")
	
