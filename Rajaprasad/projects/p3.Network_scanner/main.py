#!/usr/bin/python3
from rich import style
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
# Menu driven network scanning tool:
import nmap
import sys
# import popen
import os

console = Console()


def main_menu():
    console.print("1.Get device details", style="bold #00FF00")
    console.print("2.Scan the network for open port", style="bold #00FF00")
    console.print("3.Scan single host ", style="bold #00FF00")
    console.print("4.Scan range", style="bold #00FF00")
    console.print("5.Aggressive scan", style="bold #00FF00")
    console.print("6.Scan ARP packet", style="bold #00FF00")
    console.print("7.Scan all port only", style="bold #00FF00")
    console.print("8.Scan in verbose mode", style="bold #00FF00")
    console.print("9.Exit", style="bold #00FF00")


while True:
    main_menu()
    ch = int(Prompt.ask("Enter choice "))
    nm = nmap.PortScanner()  # Create object of nmap port scannet class
    # nm = nmap.PortScanner()

    console.print("Wait.......................", style="bold red")
    # Returns Dictinary
    # ip = input("Enter the IP : ")
    ip = str(sys.argv[1])
    # rangel = input('Enter range like 1-2000 : ')
    rangel = str(sys.argv[2])
    # interface = input("Enter interface : like -v -s S -O -e enp0s3 : ")
    # -v --> for verbose output
    verbose = sys.argv[3]
    # -s for scan
    s = sys.argv[4]
    # p --> ping scan ,looks like -sp
    # S -- > stleath scan
    # V -- > version scan
    # L --> list scan
    scanp = sys.argv[5]
    cmd = str(s+scanp)
    # -O --> os scan
    oss = str(sys.argv[6])
    # -e --> for interface name
    mis = str(sys.argv[7])
    # for interface name
    inter = str(sys.argv[8])
    # ### -A --> Aggressive scan
    # aggr = sys.argv[9]

    os_command = ' '.join([x for x in [verbose, cmd, oss, mis, inter]])

    def result():

        hostname = f"Hostname : {scan['scan'][ip]['hostnames']}"
        address = f" Address : {scan['scan'][ip]['addresses']}"
        status = f"status : {scan['scan'][ip]['status']}"

        console.print(hostname, address, status, end='\n',
                      style="bold italic #FF00FF")
        for port in scan['scan'][ip]['tcp'].items():
            console.print(
                f"{port[0]}, state : {port[1]['state']},name : {port[1]['name']},reason : {port[1]['reason']},Product : {port[1]['product']},version : {port[1]['version']},conf: {port[1]['conf']},cpe : {port[1]['cpe']}", style="bold #00FFFF")

    if ch == 1:

        try:

            scan = nm.scan(ip, rangel, os_command)
            console.print(
                f'Command : {nm.command_line()}', style="bold yellow")
            # print(f" scan Info : {nm.scaninfo()}")
            result()
        except:
            console.print("Use root priviliege", style="bold red")
    elif ch == 2:
        # nm = nmap.PortScanner()  # create object of nmap port scanner class

        try:

            scan = nm.scan(ports=rangel, arguments=os_command)
            # print(scan)
            console.print(
                f'Command : {nm.command_line()}', style="bold yellow")
            # print("scan Info : ", nm.scaninfo())
            hostname = f"Hostname : {scan['scan'][ip]['hostnames']}"
            address = f" Address : {scan['scan'][ip]['addresses']}"
            status = f"status : {scan['scan'][ip]['status']}"

            console.print(hostname, address, status, end='\n',
                          style="bold italic #FF00FF")
            for port in scan['scan'][ip]['tcp'].items():
                if port[1]['state'] == 'open':
                    console.print(
                        f"{port[0]}, state : {port[1]['state']},name : {port[1]['name']},reason : {port[1]['reason']},Product : {port[1]['product']},version : {port[1]['version']},conf: {port[1]['conf']},cpe : {port[1]['cpe']}", style="bold #00FFFF")
        except:
            console.print("Use root priviliege", style="bold red")

        # print(scan)
    elif ch == 3:
        # scan single host
        try:
            scan = nm.scan(ip)
            console.print(
                f'Command : {nm.command_line()}', style="bold yellow")
            # print("scan Info : ", nm.scaninfo())
            # print(scan)
            result()
        except:
            console.print("Use root priviliege", style="bold red")
    elif ch == 4:
        # scan range
        try:

            scan = nm.scan(ip, rangel)
            console.print(
                f'Command : {nm.command_line()}', style="bold yellow")
            # print("scan Info : ", nm.scaninfo())
            # print(scan)
            result()
        except:
            pass
    elif ch == 5:
        nmapip = "nmap -A " + ip
        scan = os.system(nmapip)
        # nmap - sp 192.168.1.1/24
        print(scan)
    elif ch == 6:
        # nmap 192.168.1.0/24 - PR
        nmap_ip = "nmap " + ip + " -PR"
        scan = os.system(nmap_ip)
        print(scan)
    elif ch == 7:
        nmap_ip = "nmap -Pn " + ip
        scan = os.system(nmap_ip)
        print(scan)
    elif ch == 8:
        nmap_ip = "nmap -v " + ip
        scan = os.system(nmap_ip)
        # print(scan)

    elif ch == 9:
        break
    else:
        console.print("Wrong choice", style="bold red")
