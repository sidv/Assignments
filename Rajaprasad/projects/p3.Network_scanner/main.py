#!/usr/bin/python3
import os
import nmap
import sys

from rich.prompt import Prompt
from rich.text import Text
from rich.console import Console


console = Console()


def cp(string):
    console.print(Text(string, style='bold #00FF00'))


def run_cmd(str):
    return os.popen(str).read()


def main_menu():
    cp("1.Get device details")
    cp("2.Scan the network for open port")
    cp("3.Scan single host ")
    cp("4.Scan range")
    cp("5.Aggressive scan")
    cp("6.Scan ARP packet")
    cp("7.Scan all port only")
    cp("8.Scan in verbose mode")
    cp("9.Exit")


while True:
    main_menu()
    ch = int(Prompt.ask("Enter choice "))
    nm = nmap.PortScanner()  # Create object of nmap port scannet class

    cp("Wait.......................")
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

        cp(hostname, address, status, end='\n')
        for port in scan['scan'][ip]['tcp'].items():
            cp(
                f"{port[0]}, state : {port[1]['state']},name : {port[1]['name']},reason : {port[1]['reason']},Product : {port[1]['product']},version : {port[1]['version']},conf: {port[1]['conf']},cpe : {port[1]['cpe']}")

    if ch == 1:

        try:

            scan = nm.scan(ip, rangel, os_command)
            cp(f'Command : {nm.command_line()}')
            # print(f" scan Info : {nm.scaninfo()}")
            result()
        except:
            cp("Use root priviliege")
    elif ch == 2:
        try:
            scan = nm.scan(ports=rangel, arguments=os_command)
            # print(scan)
            cp(f'Command : {nm.command_line()}')
            # print("scan Info : ", nm.scaninfo())
            hostname = f"Hostname : {scan['scan'][ip]['hostnames']}"
            address = f" Address : {scan['scan'][ip]['addresses']}"
            status = f"status : {scan['scan'][ip]['status']}"

            cp(hostname, address, status, end='\n')
            for port in scan['scan'][ip]['tcp'].items():
                if port[1]['state'] == 'open':
                    cp(
                        f"{port[0]}, state : {port[1]['state']},name : {port[1]['name']},reason : {port[1]['reason']},Product : {port[1]['product']},version : {port[1]['version']},conf: {port[1]['conf']},cpe : {port[1]['cpe']}")
        except:
            cp("Use root priviliege")

        # print(scan)
    elif ch == 3:
        # scan single host
        try:
            scan = nm.scan(ip)
            cp(f'Command : {nm.command_line()}')
            # print("scan Info : ", nm.scaninfo())
            # print(scan)
            result()
        except:
            cp("Use root priviliege")
    elif ch == 4:
        # scan range
        try:

            scan = nm.scan(ip, rangel)
            cp(
                f'Command : {nm.command_line()}')
            # print("scan Info : ", nm.scaninfo())
            # print(scan)
            result()
        except:
            pass
    elif ch == 5:
        cmd = "nmap -A " + ip
        # nmap - sp 192.168.1.1/24
        cp(run_cmd(cmd))
    elif ch == 6:
        # nmap 192.168.1.0/24 - PR
        cmd = "nmap " + ip + " -PR"
        cp(run_cmd(cmd))
    elif ch == 7:
        cmd = "nmap -Pn " + ip
        cp(run_cmd(cmd))
    elif ch == 8:
        cmd = "nmap -v " + ip
        cp(run_cmd(cmd))

    elif ch == 9:
        break
    else:
        console.print("Wrong choice", style="bold red")
