#!/usr/bin/python3

import pprint
from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text
import os

CONF ={}

console = Console()

def gprint(string):
	console.print(Text(string,style="bold green"))

def rprint(string): 
	console.print(Text(string,style="bold red"))

def fw_reload():
	print(os.popen("sudo firewall-cmd --reload").read())

def fw_get_active_zones():
	print("zones")
	zone = os.popen("sudo firewall-cmd --get-active-zones").read()
	CONF["ZONE"] = zone.split("\n")[0]
	print(zone)

def fw_get_details_active_zone():
	print("details")
	fw_get_active_zones()
	cmd = "ip l"
	print(os.popen(cmd))
	
	
def fw_activate():
	gprint("Activating the firewall")
	os.popen("sudo systemctl start firewalld").read()

def fw_get_status():
	state = os.popen("sudo firewall-cmd --state").read()
	if state == "running\n":
		gprint("Firewall is active")
	else:
		rprint("Firewall is not active")
		fw_activate()
	fw_get_active_zones()

def get_zone_list():
	zone_lst = os.popen("sudo firewall-cmd --get-zones").read().split(" ")
	zone_lst[-1] = zone_lst[-1][:-1] 
	return zone_lst

def fw_add_port():
	port = Prompt.ask("Enter port number : ")
	proto = Prompt.ask("Enter protocol :", choices=["tcp","udp"],default="tcp")
	zone =  Prompt.ask("Enter zone :", choices=get_zone_list(),default=CONF["ZONE"])
	cmd = "sudo firewall-cmd --add-port="+port+"/"+proto+" --zone="+zone+" --permanent "
	print(os.popen(cmd).read())

def fw_get_services():
	gprint("_________________________________________________________")
	gprint("Service List:")
	cmd = "sudo firewall-cmd --get-services"
	print(os.popen(cmd).read())
	gprint("_________________________________________________________")

def fw_add_services():
	fw_get_services()
	service = Prompt.ask("Enter service name from above list : ")
	zone =  Prompt.ask("Enter zone :", choices=get_zone_list(),default=CONF["ZONE"])
	cmd = "sudo firewall-cmd --add-service="+service+" --zone="+zone+" --permanent" 
	print(os.popen(cmd).read())

def fw_add_rule_menu():
	gprint("\t[1]Add Port")
	gprint("\t[2]Add services")
	gprint("\t[3]Add sources")
	gprint("\t[4]Back to Main menu")

def fw_add_rule():
	fw_add_rule_menu()
	ch = Prompt.ask("Enter your option : ", choices=["1", "2", "3","4"])
	if ch == "1":
		#add port
		fw_add_port()
		pass
	elif ch == "2":
		fw_add_services()
		#add services
		pass
	elif ch == "3":
		#add sources
		pass
	elif ch == "4":
		pass
	else:
		pass
		
def fw_del_port():
	port = Prompt.ask("Enter port number : ")
	proto = Prompt.ask("Enter protocol :", choices=["tcp","udp"],default="tcp")
	zone =  Prompt.ask("Enter zone :", choices=get_zone_list(),default=CONF["ZONE"])
	cmd = "sudo firewall-cmd --remove-port="+port+"/"+proto+" --zone="+zone+" --permanent "
	print(os.popen(cmd).read())

	
def fw_del_services():
	fw_get_services()
	service = Prompt.ask("Enter service name from above list : ")
	zone =  Prompt.ask("Enter zone :", choices=get_zone_list(),default=CONF["ZONE"])
	cmd = "sudo firewall-cmd --remove-service="+service+" --zone="+zone+" --permanent" 
	print(os.popen(cmd).read())


def fw_del_sources():
	source = Prompt.ask("Enter source ip address : ")
	cmd = "sudo firewall-cmd --remove-source ={ip}" 
	print(os.popen(cmd).read())
	
def fw_del_rule_menu():
	gprint("\t[1]delete Port")
	gprint("\t[2]delete services")
	gprint("\t[3]delete sources")
	gprint("\t[4]Back to Main menu")

def fw_del_rule():
	fw_del_rule_menu()
	ch = Prompt.ask("Enter your option : ", choices=["1", "2", "3","4"])
	if ch == "1":
		#del port
		fw_del_port()
		pass
	elif ch == "2":
		#del services
		fw_del_services()
		pass
	elif ch == "3":
		#del sources
		fw_del_sources()
		pass
	elif ch == "4":
		pass
	else:
		pass
		

def main_menu():
	gprint("[1] Add rules")
	gprint("[2] Delete rules")
	gprint("[3] Get Active Zones")
	gprint("[4] Get Details of Active Zones")
	gprint("[5] Reload firewall")
	gprint("[6] Exit")



if __name__ == "__main__":
	fw_get_status()
	while True:
		main_menu()
		ch = Prompt.ask("Enter your option : ", choices=["1", "2", "3","4","5","6"])
		if ch == "1":
			#Add rule
			fw_add_rule()
			pass
		elif ch == "2":
			#delete rules
			fw_del_rule()
			pass
		elif ch == "3":
			#get active zone
			fw_get_active_zones()
			pass
		elif ch == "4":
			#get active zone details
			fw_get_details_active_zone()
			pass
		elif ch == "5":
			fw_reload()
			pass
		elif ch == "6":
			#exit
			break;
		else:
			console.print(Text("Wrong option! Type option again ",style="bold red"))
