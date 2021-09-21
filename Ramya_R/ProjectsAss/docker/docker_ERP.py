# 6.Manage Docker:
#	-Status of containers
#	-Download new Image
#	-Run container
#	-Delete Container
#	-Network details of container
#	-Modify Network details of contaniner

import os
from time import sleep
from rich.console import Console
from rich.prompt import Prompt
import json
console = Console()
#console.print()

def main():
	console.print("1.Status of containers", style="bold green")
	console.print("2.Download new Image", style="bold green")
	console.print("3.Run container", style="bold green")
	console.print("4.Delete Container", style="bold green")
	console.print("5.Network details of container", style="bold green")
	console.print("6.Modify Network details of contaniner", style="bold green")
	console.print("7.Exit", style="bold Red")


while True:
	main()
	ch =  int(input("Enter choice: "))
	
	if ch == 1:
		#Status of containers
		os.system("docker container stats")
	elif ch == 2:
		#Download new Image
		#l = os.popen("docker images").read()
		img_name = input("Enter image name: ")
		l = os.popen("docker pull "+img_name).read()
		console.print(l)
		console.log(f"Task complete")
		
	elif ch == 3:
		#Run container
		img_name = input("Enter image name: ")
		container_name = input("Enter container name: ")
		c = f"docker run --name {container_name} {img_name}"
		l = os.popen(c).read()
		console.print(l)
		console.log(f"Task complete")

	elif ch == 4:
		#Delete Container
		container_name = input("Enter container name: ")
		c = f"docker rm {container_name}"
		l = os.popen(c).read()
		console.print(l)
		console.log(f"Task complete")
		
		
	elif ch == 5:
		#Network details of container
		console.print("network details")
		l = os.popen("docker network inspect bridge").read()
		l = json.loads(l)[0]
		for i in l["Containers"].values():
			print(f'{i["Name"]} | {i["MacAddress"]} | {i["IPv4Address"]}' )
		
	elif ch == 6: 
		#Modify Network details of container
		container_name = input("Enter container name: ")
		#disconnect present one
		l = os.popen("docker network disconnect bridge {container_name}").read()
		console.print(l)
		#create new network
		nw = input("Enter new ip address with mask: ")
		nw = input("Enter new network name: ")
		c = os.popen("sudo docker network create -d bridge -- subnet={ip} {nw}").read()
		#connect container to new network
		nwn = input("Enter created network name: ")
		container_name = input("Enter container name: ")
		cmd = os.popen("docker network connect {nwn} {container_name}").read()
		console.print(cmd)
		console.log(f"Task complete")
		
	elif ch == 7:
		break;
	else:
		print("Wrong Choice")
	

