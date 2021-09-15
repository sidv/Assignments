
import os
from rich.prompt import Prompt
from rich.text import Text
from rich.console import Console
from script import *

console = Console()


def cp(string):
    console.print(Text(string, style='bold #00FF00'))


def run_cmd(str):
    return os.popen(str).read()


def display_aval_RAM():
    cmd = 'free -m | tr -s " " | cut -d " " -f4 | head -n 2 | tail -n 1'
    cp(f'Available memory on device => {run_cmd(cmd)} mb')


def display_load_avg():
    cmds = 'cat /proc/loadavg'
    cmd = Prompt.ask('Enter the command', choices=[
                     f'{cmds}', 'uptime', 'w'], default='uptime')
    cp(run_cmd(cmd))


def hostname_details():
    cmd = 'hostnamectl status'
    cp(run_cmd(cmd))


def process_count():
    cmd = 'ps -a | wc -l'
    cp(f' {run_cmd(cmd)} processes running on system ')


def display_uptime():
    cmd = 'uptime | cut -d " " -f2,3'
    cp(f'Uptime ==>  {run_cmd(cmd)}')
