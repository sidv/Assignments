#!/usr/bin/python3
from script import *


def main_menu():
    cp('-'*40)
    cp('[1].Assign ip address')
    cp('[2].Delete ip address')
    cp('[3].Display ip address')
    cp('[4].Display all interfaces')
    cp('[5].Configure Routing')
    console.print(
        '[bold #00FF00][6].Turn On/[red]Off[/red] interface[/bold #00FF00]')
    cp('[7].Add ARP entry')
    cp('[8].Delete ARP Entry')
    cp('[9].Restart Network')
    cp('[10].Change hostname')
    cp('[11].Add DNS server entry')
    rp('[12].Exit')
    cp('-'*40)


def Exit():
    exit()


op = {
    '1': ip_cmd,
    '2': ip_cmd_del,
    '3': ip_display,
    '4': display_all_interface,
    '5': configure_routing,
    '6': On_Off_interface,
    '7': add_ARP_entry,
    '8': del_arp_entry,
    '9': restart_network,
    '10': change_host_name,
    '11': add_dns_server,
    '12': Exit
}

if __name__ == '__main__':
    while True:
        main_menu()
        ch = Prompt.ask('Enter choice :', choices=[
                        str(x) for x in range(1, 13)], default='1')

        op[ch]()
