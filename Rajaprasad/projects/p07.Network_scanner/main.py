#!/usr/bin/python3

# Menu driven network scanning tool:
import nmap
import sys
import os

from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text

console = Console()


def rp(string):
    return console.print(string, style='bold red')


def gp(string):
    return console.print(string, style='bold green')


def pp(string):
    return console.print(string, style='bold #FF00FF ')


# defining error handler decorator
def Error_Handler(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            rp(f'exception flew by! , {func.__name__} use sudo instead ')
        else:
            gp('commands executed ....')
        finally:
            console.print('execution over !!!!', style='bold #00FFFF ')
    return wrapper


# define decorator
def decorate(func):

    def wrap_func():
        pp('*'*100)
        func()
        console.print('*'*100, style='bold #00FFFF ')

    return wrap_func


def run_cmd(string):
    return os.popen(string).read()


# default value start
pp('Wait.......................')
# Enter the IP :
IP = str(sys.argv[1])
# RANGEL = input('Enter range like 1-2000 : ')
RANGEL = str(sys.argv[2])
# -v --> for verbose output
VERBOSE = sys.argv[3]
# -s for scan
s = sys.argv[4]
# p --> ping scan ,looks like -sp
# S -- > stleath scan
# V -- > version scan
# L --> list scan
SCANP = sys.argv[5]
CMD = str(s+SCANP)
# -O --> os scan
OSS = str(sys.argv[6])
# -e --> for interface name
MIS = str(sys.argv[7])
# for interface name
INTERFACE = str(sys.argv[8])
# ### -A --> Aggressive scan
OS_COMMAND = ' '.join([x for x in [VERBOSE, CMD, OSS, MIS, INTERFACE]])
# default value end


# @decorate
def result(scan):

    hostname = f"Hostname : {scan['scan'][IP]['hostnames']}"
    address = f" Address : {scan['scan'][IP]['addresses']}"
    status = f"status : {scan['scan'][IP]['status']}"

    gp('\n'.join(f'{hostname}, {address}, {status}'.split(',')))
    for port in scan['scan'][IP]['tcp'].items():
        pp(
            f"{port[0]}, state : {port[1]['state']},name : {port[1]['name']},reason : {port[1]['reason']},Product : {port[1]['product']},version : {port[1]['version']},conf: {port[1]['conf']},cpe : {port[1]['cpe']}".split(','))


@Error_Handler
def device_detail():
    scan = nm.scan(IP, RANGEL, OS_COMMAND)
    pp(f'Command : {nm.command_line()}')
    # print(f" scan Info : {nm.scaninfo()}")
    result(scan)


def scan_open_port_only():
    try:
        scan = nm.scan(ports=RANGEL, arguments=OS_COMMAND)
        pp(f'Command : {nm.command_line()}')
        # print("scan Info : ", nm.scaninfo())
        hostname = f"Hostname : {scan['scan'][IP]['hostnames']}"
        address = f" Address : {scan['scan'][IP]['addresses']}"
        status = f"status : {scan['scan'][IP]['status']}"
        gp('\n'.join(f'{hostname}, {address}, {status}'.split(',')))
        for port in scan['scan'][IP]['tcp'].items():
            if port[1]['state'] == 'open':
                pp(
                    f"{port[0]}, state : {port[1]['state']},name : {port[1]['name']},reason : {port[1]['reason']},Product : {port[1]['product']},version : {port[1]['version']},conf: {port[1]['conf']},cpe : {port[1]['cpe']}".split(','))
    except:
        rp('Use sudo instead')


@Error_Handler
def scan_single_host():
    scan = nm.scan(IP)
    pp(f'Command : {nm.command_line()}')
    result(scan)


@Error_Handler
def scan_range():
    scan = nm.scan(IP, RANGEL)
    pp(f'Command : {nm.command_line()}')
    result(scan)


@Error_Handler
@decorate
def aggressive_scan():
    command = f'nmap -A {IP}'
    gp(run_cmd(command))


@Error_Handler
@decorate
def scan_arp_pkt():
    command = f'nmap {IP} -PR'
    gp(run_cmd(command))


@Error_Handler
@decorate
def scan_all_port_only():
    command = f'nmap -Pn {IP}'
    gp(run_cmd(command))


@Error_Handler
@decorate
def scan_verbose_mode():
    command = f'nmap -v {IP}'
    gp(run_cmd(command))


@decorate
def main_menu():
    gp('[1].Get device details')
    gp('[2].Scan the network for open port')
    gp('[3].Scan single host ')
    gp('[4].Scan range')
    gp('[5].Aggressive scan')
    gp('[6].Scan ARP packet')
    gp('[7].Scan all port only')
    gp('[8].Scan in VERBOSE mode')
    rp('[9].Exit')


def Exit():
    exit()


op = {
    '1': device_detail,
    '2': scan_open_port_only,
    '3': scan_single_host,
    '4': scan_range,
    '5': aggressive_scan,
    '6': scan_arp_pkt,
    '7': scan_all_port_only,
    '8': scan_verbose_mode,
    '9': Exit
}

while True:
    main_menu()
    ch = Prompt.ask('Enter choice: ', choices=[
                    str(x) for x in range(1, 10)], default='1')
    nm = nmap.PortScanner()  # Create object of nmap port scannet class
    op[ch]()
