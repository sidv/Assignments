import os
from rich.prompt import Prompt
from rich.console import Console
from rich.text import Text


console = Console()


def cp(string):
    console.print(Text(string, style='bold #00FF00'))


def rp(string):
    return console.print(string, style='bold red')


def pp(string):
    return console.print(string, style='bold #FF00FF ')


def run_cmd(str):
    return os.popen(str).read()

# defining error handler decorator


def Error_Handler(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            rp(f'exception flew by! , {func.__name__} use sudo instead ')
        else:
            pp('commands executed ....')
        finally:
            pp('execution over !!!!')
            pp('*'*40)
    return wrapper


def ip():
    ip = input('Enter ip address to add on interface : ')
    if len(ip.split('.')) == 4:
        return ip


def interfaces():
    s = os.popen(
        'ip l | cut -d":" -f2 | tr -d " " | cut -d" " -f1').read()
    interface = s.split('\n')[:-2:2]
    return interface


def interface_choice():
    s = os.popen(
        'ip l | cut -d":" -f2 | tr -d " " | cut -d" " -f1').read()
    interfaces = s.split('\n')[:-2:2]
    interface_choice = Prompt.ask(
        "Enter Interface : ", choices=interfaces, default="enp0s3")
    return interface_choice


@Error_Handler
def ip_cmd():
    # Assign ip address
    cmd = f'ip address add {ip()} dev {interface_choice()}'
    cp(run_cmd(cmd))
    cp('Ip address assigned successfully')


@Error_Handler
def ip_cmd_del():
    # Delete Ip address
    cmd = f'sudo ip address del {ip()} dev {interface_choice()}'
    cp(run_cmd(cmd))
    cp('Ip address Deleted successfully')


@Error_Handler
def ip_display():
    # show ip address of all interfaces
    cmd = f'ip -c -br address'
    cp(run_cmd(cmd))


@Error_Handler
def display_all_interface():
    cmd = 'ip l'
    cp(f'All interfaces name  => {interfaces()}  Details => {run_cmd(cmd)}')


@Error_Handler
def configure_routing():
    network_addr = input('Enter network Address with /mask : ')
    getway_ip = input('Enter Gateway ip address : ')
    if len(network_addr.split('.')) == 4 and len(getway_ip.split('.')) == 4:
        cmd = f'ip r add {network_addr} via {getway_ip}'
        cp(run_cmd(cmd))
        cp('Roting configuration completed !')


@Error_Handler
def On_Off_interface():
    cp('[on].Turned on interface')
    cp('[off].Turned off interface')
    choice = Prompt.ask('Enter choice : ', choices=['on', 'off'], default='on')

    if choice == 'on':
        cmd = f'sudo ip link set dev {interface_choice()}  down'
        cp(f' turned off  | Details => {pp(run_cmd(cmd))}')

    elif choice == 'off':
        cmd = f'sudo ip link set dev {interface_choice()}  up'
        cp(f' turned on | Details => {pp(run_cmd(cmd))} ')


@Error_Handler
def add_ARP_entry():
    mac = Prompt.ask('Enter mac address : ')
    cmd = f'ip n add {ip()} lladdr {mac} dev {interface_choice()} nud permanent'
    run_cmd(cmd)
    cp('ARP Entry added successfully ')


@Error_Handler
def del_arp_entry():
    cmd = f'ip n del {ip()} dev {interface_choice()}'
    run_cmd(cmd)
    cp('ARP Entry deleted successfully ')


@Error_Handler
def restart_network():
    cmd = 'sudo systemctl restart networking'
    cmd2 = 'sudo systemctl status networking'
    cp(run_cmd(cmd))
    cp('Network services restarted ')
    cp(os.popen(cmd2).read())


@Error_Handler
def change_host_name():
    host_name = input("Enter new host name :")
    cmd = f'hostnamectl set-hostname {host_name}'
    run_cmd(cmd)
    cp(f'new host name {host_name} set successfully ')


@Error_Handler
def add_dns_server():
    pp('adding dns server')
    cp('first : nameserver 8.8.8.8 write in this format')
    pp('second : ctrl + d  to exit ')
    cmd = 'sudo cat  >> /etc/resolv.conf'
    cp(run_cmd(cmd))
    cp('Nameserver added successfully  ')
