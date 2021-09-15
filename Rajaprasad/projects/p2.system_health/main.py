#!/usr/bin/python3
import os
from rich.prompt import Prompt
from rich import style
from rich.console import Console
from script import *

console = Console()


def main_menu():
    console.print('-'*20, style='bold #00FF00')
    console.print('1.Display available RAM', style='bold #00FF00')
    console.print('2.Display load average', style='bold #00FF00')
    console.print('3.Display Hostname details', style='bold #00FF00')
    console.print('4.Display All process count', style='bold #00FF00')
    console.print('5.Display uptime', style='bold #00FF00')
    console.print('6.Exit', style='bold #00FF00')
    console.print('-'*20, style='bold #00FF00')


while True:
    main_menu()
    ch = int(input('Enter choice : '))
    if ch == 1:
        display_aval_RAM()
    elif ch == 2:
        display_load_avg()
    elif ch == 3:
        hostname_details()
    elif ch == 4:
        process_count()
    elif ch == 5:
        display_uptime()
    elif ch == 6:
        break
    else:
        console.print('oops ! wrong option  ', style='bold red')
