#!/usr/bin/python3

#Menu driven network scanning tool:
import nmap

while True:
	print("1.Get device details")
	print("2.Scan the network for open port")
	print("3.Exit")
	ch =  int(input("Enter choice: "))
	if ch == 1:
		nm = nmap.PortScanner() #Create object of nmap port scannet class
		ip = input("Enter the IP : ")
		print("Wait.......................")
		try:
			scan = nm.scan(ip,"1-2000","-v -sS -O -e ens33") #Returns Dictinary
			print(scan)
			print(scan['scan'][ip]['addresses']['mac'])
			for port in scan["scan"][ip]['tcp'].items():
				print(f"{port[0]}, {port[1]['state']} , {port[1]['name']}")
		except:
			print("Use root priviliege")
	elif ch == 2:
		nm = nmap.PortScanner() #create object of nmap port scanner class
		print("Wait........................")
		try:
			scan = nm.scan(ports="1-5000",arguments = "-sS -O -e ens33")
		except:
			print("Use root priviliege")
		print(scan)
	elif ch == 3:
		break;
	else:
		print("Wrong Choice")
	

