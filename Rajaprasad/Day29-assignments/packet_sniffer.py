#!/usr/bin/python3
import subprocess  # Create another processs
from datetime import datetime
from scapy.all import *
import sys
from rich.console import Console

console = Console()

# datetime object containing current date and time
now = datetime.now()

console.print("Using Sudo", style="bold red")
# Packet sniffer script using scapy

net_iface = str(sys.argv[1])

# promisceous mode transfer the interface data packets to cpu to processs and you capture from there
# creating another process to run command
subprocess.call(["ifconfig", net_iface, "promisc"])

#input("Enter the packet count you want to capture : ")
num_of_pkt = int(sys.argv[2])

#input("Enter the time how long(in sec) run to capture : ")
time_sec = int(sys.argv[3])

#input("Enter the protocol( arp | icmp | all ) : ")

proto = str(sys.argv[4])

# sniff function call it and pass every packet in byte format


def logs(packet):

    console.print('-'*20, style="bold #00FF00")
    print(f'Time : {now}')
    # packet.show()
    source_mac = f'SRC_MAC: {str(packet[0].src)}'
    destination_mac = f'DEST_MAC : {str(packet[0].dst)}'
    # type_of_ip = f'IP Type : IPv{str(packet[0].version)}'
    console.print(source_mac, destination_mac, style="#FF00FF")
    console.print('-'*20, style="#00FF00")


if proto == "all":
    sniff(iface=net_iface, count=num_of_pkt,
          timeout=time_sec, prn=logs)  # sniffing packet
elif proto == "arp":
    sniff(iface=net_iface, count=num_of_pkt,
          timeout=time_sec, prn=logs)  # sniffing packet
elif proto == "icmp":
    sniff(iface=net_iface, count=num_of_pkt,
          timeout=time_sec, prn=logs)  # sniffing packet
else:
    print("Wrong protocol")
