
#!/usr/bin/python3
import os
from rich.prompt import Prompt
from rich import style
from rich.console import Console
from script import *

console = Console()


def main_menu():
    console.print('-'*20, style='bold #00FF00')
    console.print('1.Assign ip address', style='bold #00FF00')
    console.print('2.Delete ip address', style='bold #00FF00')
    console.print('3.Display ip address', style='bold #00FF00')
    console.print('4.Display all interfaces', style='bold #00FF00')
    console.print('5.Configure Routing', style='bold #00FF00')
    console.print('6.Turn On/Off interface', style='bold #00FF00')
    console.print('7.Add ARP entry', style='bold #00FF00')
    console.print('8.Delete ARP Entry', style='bold #00FF00')
    console.print('9.Restart Network', style='bold #00FF00')
    console.print('10.Change hostname', style='bold #00FF00')
    console.print('11.Add DNS server entry', style='bold #00FF00')
    console.print('12.Exit', style='bold #00FF00')
    console.print('-'*20, style='bold #00FF00')


while True:
    main_menu()
    ch = int(input('Enter choice : '))
    if ch == 1:
        ip_cmd()

    elif ch == 2:
        ip_cmd_del()

    elif ch == 3:
        ip_display()

    elif ch == 4:
        display_all_interface()

    elif ch == 5:
        configure_routing()

    elif ch == 6:
        On_Off_interface()

    elif ch == 7:
        add_ARP_entry()

    elif ch == 8:
        del_arp_entry()

    elif ch == 9:
        restart_network()

    elif ch == 10:
        change_host_name()

    elif ch == 11:
        add_dns_server()

    elif ch == 12:
        break

    else:
        console.print(
            'oops ! Wrong option,  please choose correct option below ', style='Bold #F91308')
