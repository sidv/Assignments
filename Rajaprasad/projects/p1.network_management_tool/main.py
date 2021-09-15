#!/usr/bin/python3
from script import *


def main_menu():
    cp('-'*20)
    cp('1.Assign ip address')
    cp('2.Delete ip address')
    cp('3.Display ip address')
    cp('4.Display all interfaces')
    cp('5.Configure Routing')
    cp('6.Turn On/Off interface')
    cp('7.Add ARP entry')
    cp('8.Delete ARP Entry')
    cp('9.Restart Network')
    cp('10.Change hostname')
    cp('11.Add DNS server entry')
    cp('12.Exit')
    cp('-'*20)


if __name__ == '__main__':
    while True:
        main_menu()
        ch = Prompt.ask('Enter choice :', choices=[
                        str(x) for x in range(1, 13)], default='1')

        if ch == '1':
            ip_cmd()

        elif ch == '2':
            ip_cmd_del()

        elif ch == '3':
            ip_display()

        elif ch == '4':
            display_all_interface()

        elif ch == '5':
            configure_routing()

        elif ch == '6':
            On_Off_interface()

        elif ch == '7':
            add_ARP_entry()

        elif ch == '8':
            del_arp_entry()

        elif ch == '9':
            restart_network()

        elif ch == '10':
            change_host_name()

        elif ch == '11':
            add_dns_server()

        elif ch == '12':
            break

        else:
            console.print(
                'oops ! Wrong option,  please choose correct option below ', style='bold red')
