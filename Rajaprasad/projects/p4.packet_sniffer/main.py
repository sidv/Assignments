#!/usr/bin/python3

# Packet sniffer script using scapy


import subprocess  # Create another processs
from datetime import datetime
from scapy.all import *
import sys
from rich.console import Console
from rich.text import Text

console = Console()


def cp(string):
    console.print(Text(string, style='bold #00FF00'))


def rp(string):
    console.print(Text(string, style='bold red'))


def pp(string):
    console.print(Text(string, style='bold italic #FF00FF '))


try:
    now = datetime.now()
    net_iface = str(sys.argv[1])
    # promisceous mode transfer the interface data packets to cpu to processs and you capture from there
    # creating another process to run command
    subprocess.call(["ifconfig", net_iface, "promisc"])
    # Enter the packet count you want to capture
    num_of_pkt = int(sys.argv[2])
    # Enter the time how long(in sec) run to capture
    time_sec = int(sys.argv[3])
    # Enter the protocol( arp | icmp | all )
    proto = str(sys.argv[4])
    # sniff function call it and pass every packet in byte format

    # @Error_Handler

    def logs(packet):

        cp('-'*20)
        pp(f'Time : {now}')
        # packet.show()
        source_mac = f'SRC_MAC: {str(packet[0].src)}'
        destination_mac = f'DEST_MAC : {str(packet[0].dst)}'
        cp(f'{source_mac}, {destination_mac}')
        pp('-'*20)

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
        console.print("Wrong protocol", style='bold red')
except:
    rp('Exception flew by, Use sudo instead')
