import os
from rich.prompt import Prompt
from rich import style
from rich.console import Console

console = Console()


def ip_cmd():
    # Assign ip address
    ip = input('Enter ip address to add on interface : ')
    if len(ip.split('.')) == 4:
        s = os.popen(
            'ip l | cut -d":" -f2 | tr -d " " | cut -d" " -f1').read()
        interfaces = s.split('\n')[:-2:2]
        interface_choice = Prompt.ask(
            "Enter Interface : ", choices=interfaces, default="enp0s3")
        command = f'ip address add {ip} dev {interface_choice}'
        res = os.popen(command).read()
        console.print(res, style="bold italic #FF00FF")
        console.print('Ip address assigned successfully', style='bold green')


def ip_cmd_del():
    # Delete Ip address
    ip = input('Enter ip address to delete from interface : ')
    if len(ip.split('.')) == 4:
        s = os.popen(
            'ip l | cut -d":" -f2 | tr -d " " | cut -d" " -f1').read()
        interfaces = s.split('\n')[:-2:2]
        interface_choice = Prompt.ask(
            "Enter Interface : ", choices=interfaces, default="enp0s3")
        command = f'sudo ip address del {ip} dev {interface_choice}'
        res = os.popen(command).read()
        console.print(res, style="bold italic #FF00FF")
        console.print('Ip address Deleted successfully', style='bold red')


def ip_display():
    # show ip address of all interfaces
    command = f'ip -c -br address'
    res = os.popen(command).read()
    console.print(res, style=" italic ")


def display_all_interface():
    s = os.popen(
        'ip l | cut -d":" -f2 | tr -d " " | cut -d" " -f1').read()
    interfaces = s.split('\n')[:-2:2]
    command = 'ip l'
    res = os.popen(command).read()
    console.print(
        f'All interfaces name  => {interfaces}  Details => {res}', style='bold #5028B2 ')


def configure_routing():
    network_addr = input('Enter network Address with /mask : ')
    getway_ip = input('Enter Gateway ip address : ')
    if len(network_addr.split('.')) == 4 and len(getway_ip.split('.')) == 4:
        cmd = f'ip r add {network_addr} via {getway_ip}'
        res = os.popen(cmd).read()
        console.print(res, style='bold grey')
        console.print('Roting configuration completed !',
                      style='bold italic #74EFA2')


def On_Off_interface():
    console.print('1.Turned off interface ', style='bold #00FF00')
    console.print('2.Turned on interface', style='bold #00FF00')
    choice = Prompt.ask('Enter choice : ', choices=['1', '2'], default='1')

    s = os.popen(
        'ip l | cut -d":" -f2 | tr -d " " | cut -d" " -f1').read()
    interfaces = s.split('\n')[:-2:2]
    interface_choice = Prompt.ask(
        "Enter Interface : ", choices=interfaces, default="enp0s3")

    if choice == 1:

        cmd = f'ip link set dev {interface_choice}  down'
        res = os.popen(cmd).read()
        console.print(
            f'{interface_choice} turned off  | Details => {res}', style='bold red')

    elif choice == 2:
        cmd = f'ip link set dev {interface_choice}  up'
        res = os.popen(cmd).read()
        console.print(
            f'{interface_choice} turned on | Details => {res} ', style='bold red')

    else:
        console.print('Wrong option choosed', style='red')


def add_ARP_entry():
    ip = input('Enter ip address  : ')
    if len(ip.split('.')) == 4:
        s = os.popen(
            'ip l | cut -d":" -f2 | tr -d " " | cut -d" " -f1').read()
        interfaces = s.split('\n')[:-2:2]
        interface_choice = Prompt.ask(
            "Enter Interface : ", choices=interfaces, default="enp0s3")
        arp_cache = os.popen('ip n show | cut -d " " -f5').read()
        cmd = f'ip n add {ip} lladdr {arp_cache} dev {interface_choice} nud permanent'
        res = os.popen(cmd).read()
        console.print('ARP Entry added successfully ', style='bold #CAEF74')


def del_arp_entry():
    ip = input('Enter ip address : ')
    if len(ip.split('.')) == 4:
        s = os.popen(
            'ip l | cut -d":" -f2 | tr -d " " | cut -d" " -f1').read()
        interfaces = s.split('\n')[:-2:2]
        interface_choice = Prompt.ask(
            "Enter Interface : ", choices=interfaces, default="enp0s3")
        cmd = f'ip n del {ip} dev {interface_choice}'
        res = os.popen(cmd).read()
        console.print('ARP Entry deleted successfully ', style='bold #F90D02')


def restart_network():
    cmd = 'sudo systemctl restart networking'
    cmd2 = 'sudo systemctl status networking'
    os.popen(cmd).read()
    console.print('Network services restarted ', style='bold #16F902')
    console.print(os.popen(cmd2).read(), style='bold green')


def change_host_name():
    host_name = input("Enter new host name :")
    cmd = f'hostnamectl set-hostname {host_name}'
    os.popen(cmd).read()
    console.print(
        f'new host name {host_name} set successfully ', style='bold #F90D02')


def add_dns_server():

    print('adding dns server')
    print('first : nameserver 8.8.8.8 write in this format')
    print('second : ctrl + d  to exit ')
    cmd = 'sudo cat  >> /etc/resolv.conf'
    print(os.popen(cmd).read())
    console.print('Nameserver added successfully  ', style='bold #F90D02')
