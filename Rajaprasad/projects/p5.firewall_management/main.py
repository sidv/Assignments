#!/usr/bin/python3
from add_rules import *

# -------- delete rules


def fw_delete_rules_menu():
    gprint("\t[1]Remove Port")
    gprint("\t[2]Remove services")
    gprint("\t[3]Remove source port")
    gprint("\t[4]Remove sources")
    gprint("\t[5]Remove zone binding for certain interface")
    rprint("\t[6]Back to Main menu")


def fw_remove_port():
    cmd = f'sudo firewall-cmd --remove-port={ports()}/{protos()} --permanent --zone={zones()}'
    rprint(run_cmd(cmd))


def fw_remove_services():
    fw_get_services()
    service = Prompt.ask("Enter service name from above list : ")
    cmd = f'sudo firewall-cmd --remove-service={service} --zone={zones()} --permanent'
    rprint(run_cmd(cmd))


def fw_rmv_src_port():
    cmd = f'sudo firewall-cmd --remove-source-port={ports()}/{protos()} --permanent --zone={zones()}'
    rprint(run_cmd(cmd))


def fw_rmv_sources():
    ip = Prompt.ask('Enter source ip address : ')
    cmd = f'sudo firewall-cmd --remove-source={ip}'
    rprint(run_cmd(cmd))


def interface_choice():
    s = os.popen(
        'ip l | cut -d":" -f2 | tr -d " " | cut -d" " -f1').read()
    interfaces = s.split('\n')[:-2:2]
    interface_choice = Prompt.ask(
        "Enter Interface : ", choices=interfaces, default="enp0s3")
    return interface_choice


def fw_rmv_zone():
    cmd = f'sudo firewall-cmd --zone=public --remove-interface={interface_choice()} --permanent'
    rprint(run_cmd(cmd))


def fw_delete_rules():
    fw_delete_rules_menu()
    ch = Prompt.ask("Enter your option : ", choices=[
                    str(x) for x in range(1, 7)], default='1')
    if ch == '1':
        fw_remove_port()
    elif ch == '2':
        fw_remove_services()
    elif ch == '3':
        fw_rmv_src_port()
    elif ch == '4':
        fw_rmv_sources()
    elif ch == '5':
        fw_rmv_zone()
    elif ch == '6':
        pass
    else:
        pass

# ---- active zones


def fw_get_active_zones():
    cmd = 'sudo firewall-cmd --get-active-zones'
    zone = run_cmd(cmd)
    CONF["ZONE"] = zone.split("\n")[0]
    gprint(zone)

# ------- active Zones details


def fw_get_detail_active_zone():
    fw_get_active_zones()
    gprint('-'*100)
    cmd = 'ip l'
    gprint(run_cmd(cmd))
    rprint('-'*100)

#----- reload


def fw_reload():
    rprint('-'*100)
    cmd = 'sudo firewall-cmd --reload'
    gprint(run_cmd(cmd))
    rprint('-'*100)


def fw_activate():
    gprint("Activating the firewall")
    cmd = "sudo systemctl start firewalld"
    run_cmd(cmd)


def fw_get_status():
    cmd = "sudo firewall-cmd --state"
    state = run_cmd(cmd)
    if state == "running\n":
        gprint("Firewall is active")
    else:
        rprint("Firewall is not active")
        fw_activate()
    fw_get_active_zones()
    gprint('-'*100)


def main_menu():
    gprint("[1] Add rules")
    gprint("[2] Delete rules")
    gprint("[3] Get Active Zones")
    gprint("[4] Get Details of Active Zones")
    gprint("[5] Reload firewall")
    rprint("[6] Exit")
    rprint('-'*100)


if __name__ == "__main__":
    fw_get_status()
    while True:
        main_menu()
        ch = Prompt.ask("Enter your option : ", choices=[
                        str(x) for x in range(1, 7)])
        if ch == "1":
            # Add rule
            fw_add_rule()
        elif ch == "2":
            # delete rules
            fw_delete_rules()
        elif ch == "3":
            # get active zones
            fw_get_active_zones()
        elif ch == "4":
            # get active zone details
            fw_get_detail_active_zone()
        elif ch == "5":
            # reload
            fw_reload()
        elif ch == "6":
            # exit
            break
        else:
            console.print(
                Text("Wrong option! Type option again ", style="bold red"))
