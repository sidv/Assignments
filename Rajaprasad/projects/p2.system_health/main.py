#!/usr/bin/python3
from script import *


def main_menu():
    cp('-'*40)
    cp('[1].Display available RAM')
    cp('[2].Display load average')
    cp('[3].Display Hostname details')
    cp('[4].Display All process count')
    cp('[5].Display uptime')
    rp('[6].Exit')
    cp('-'*40)


def Exit():
    exit()


op = {
    '1': display_aval_RAM,
    '2': display_load_avg,
    '3': hostname_details,
    '4': process_count,
    '5': display_uptime,
    '6': Exit
}

if __name__ == '__main__':
    while True:
        main_menu()
        ch = Prompt.ask('Enter choice : ', choices=[
                        str(x) for x in range(1, 7)], default='1')
        op[ch]()
