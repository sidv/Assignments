
import os
from rich.prompt import Prompt
from rich import style
from rich.console import Console
from script import *

console = Console()


def display_aval_RAM():
    mem = os.popen(
        'free -m | tr -s " " | cut -d " " -f4 | head -n 2 | tail -n 1').read()
    console.print(
        f'Available memory on device => {mem} mb', style='bold #F908E6 ')


def display_load_avg():
    cmds = 'cat /proc/loadavg'
    cmd = Prompt.ask('Enter the command', choices=[
                     f'{cmds}', 'uptime', 'w'], default='uptime')
    res = os.popen(cmd).read()
    console.print(res, style='italic #7C53E7 ')


def hostname_details():
    cmd = 'hostnamectl status'
    res = os.popen(cmd).read()
    console.print(res, style='bold #01F9EB ')


def process_count():
    cmd = 'ps -a | wc -l'
    res = os.popen(cmd).read()
    console.print(f' {res} processes running on system ',
                  style='bold #01F9EB ')


def display_uptime():
    cmd = 'uptime | cut -d " " -f2,3'
    res = os.popen(cmd).read()
    console.print(f'Uptime ==>  {res}', style='italic blue')
