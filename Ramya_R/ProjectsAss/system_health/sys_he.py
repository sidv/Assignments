import os
from time import sleep
from rich.console import Console
from rich.color import Color
from rich.prompt import Prompt
from rich import pretty

import json

console = Console()
console.print()

def main():
	console.print("1.Display available RAM", style="bold green")
	console.print("2.Display Load avearge", style="bold green")
	console.print("3.Display Hostname details", style="bold green")
	console.print("4.Display All process count", style="bold green")
	console.print("5.Display uptime", style="bold green")
	console.print("6.Exit", style="bold red")
	
while True:
	main()
	ch =  int(input("Enter choice: "))
	
	#ip = input("Enter the IP : ")
	
	
	if ch == 1:
		#Display available RAM
		console.print("Display available RAM")
		#re = os.popen("free -m").read()
		#console.print(re)
		cmd = 'free -m | tr -s " " | cut -d " " -f7'
		res = os.popen(cmd).read()
		console.print(res)
		
	elif ch == 2:
		#Display Load avearge
		console.print("Display Load avearge")
		cmd = 'cat /proc/loadavg'
		res = os.popen(cmd).read()
		console.print(res)
		
	elif ch == 3:
		#Display Hostname details
		console.print("Display Hostname details")
		cmd = 'hostnamectl status'
		res = os.popen(cmd).read()
		console.print(res)
	elif ch == 4:
		#Display All process count
		console.print("Display All process count")
		cmd = 'ps -a |wc -l'
		res = os.popen(cmd).read()
		console.print(res)
		
	elif ch == 5:
		#Display uptime
		console.print("Display uptime")
		#res = os.popen("uptime").read()
		cmd = 'uptime | cut -d " " -f1,2,3'
		res = os.popen(cmd).read()
		console.print(res)
	elif ch == 6:
		break;
	else:
		console.print("Wrong Choice")
	
