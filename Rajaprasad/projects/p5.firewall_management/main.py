#!/usr/bin/python3
from add_rules import *

# -------- delete rules starts ------------


def fw_delete_rules_menu():
    gprint('\t[1]Remove Port')
    gprint('\t[2]Remove services')
    gprint('\t[3]Remove source port')
    gprint('\t[4]Remove sources')
    gprint('\t[5]Remove zone binding for certain interface')
    rprint('\t[6]Back to Main menu')


@Error_Handler
def fw_remove_port():
    cmd = f'sudo firewall-cmd --remove-port={ports()}/{protos()} --permanent --zone={zones()}'
    rprint(run_cmd(cmd))


@Error_Handler
def fw_remove_services():
    fw_get_services()
    service = Prompt.ask('Enter service name from above list : ')
    cmd = f'sudo firewall-cmd --remove-service={service} --zone={zones()} --permanent'
    rprint(run_cmd(cmd))


@Error_Handler
def fw_rmv_src_port():
    cmd = f'sudo firewall-cmd --remove-source-port={ports()}/{protos()} --permanent --zone={zones()}'
    rprint(run_cmd(cmd))


@Error_Handler
def fw_rmv_sources():
    ip = Prompt.ask('Enter source ip address : ')
    cmd = f'sudo firewall-cmd --remove-source={ip}'
    rprint(run_cmd(cmd))


@Error_Handler
def fw_rmv_zone():
    cmd = f'sudo firewall-cmd --zone=public --remove-interface={interface_choice()} --permanent'
    rprint(run_cmd(cmd))


def fw_delete_rules():
    fw_delete_rules_menu()
    ch = Prompt.ask('Enter your option : ', choices=[
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
# ---- delete rules end-------------------------------------


# allow_deny_rule starts --------------
@decorate
def allow_deny_rule_menu():
    gprint('\t\t[1]Allow/Deny the host/IP')
    gprint('\t\t[2]Allow/Deny a subnet(Network)')
    gprint('\t\t[3]Allow/Deny the interface')
    gprint('\t\t[4]Allow/Deny Port')
    gprint('\t\t[5]Allow/Deny App')
    gprint('\t\t[6]Allow/Deny app layer protocols')
    gprint('\t\t[7]Disable firewall')
    rprint('\t\t[8]Back to main menu')


@decorate
def fw_enable():
    cmd = 'sudo ufw enable'
    gprint(run_cmd(cmd))


@Error_Handler
def allow_deny_ip():
    # Allow the host/IP
    cmd = f'sudo ufw {allow_deny()} from {ip_addr()}'
    gprint(run_cmd(cmd))


@Error_Handler
def allow_deny_subnet():
    # Allow a subnet(Network)
    subnet = Prompt.ask('Enter subnet address : ')
    cmd = f'sudo ufw {allow_deny()} from {subnet}'
    gprint(run_cmd(cmd))


@Error_Handler
def allow_deny_interface():
    # Allow the interface
    cmd = f'sudo ufw {allow_deny()} in on {interface_choice} from {ip_addr()}'
    gprint(run_cmd(cmd))


@Error_Handler
def allow_deny_port():
    # Allow Port
    cmd = f'sudo ufw {allow_deny()} {ports()}'
    gprint(run_cmd(cmd))


@Error_Handler
def allow_deny_app():
    # Allow app
    cmd = 'sudo ufw app list'
    gprint(run_cmd(cmd))
    apps = Prompt.ask('Enter app name from above list : ')
    cmd = f'sudo ufw {allow_deny()} "{apps}"'
    gprint(run_cmd(cmd))


@Error_Handler
def ad_app_lyr_protocol():
    # Allow app layer protocols
    proto = Prompt.ask('Enter protocol :', choices=[
        'http', 'https'], default='https')
    cmd = f'sudo ufw {allow_deny()} {proto}'
    gprint(run_cmd(cmd))


def allow_deny_rule():
    fw_enable()
    allow_deny_rule_menu()
    ch = Prompt.ask('Enter your option : ', choices=[
                    str(x) for x in range(1, 8)], default='1')
    if ch == '1':
        allow_deny_ip()
    elif ch == '2':
        allow_deny_subnet()
    elif ch == '3':
        allow_deny_interface()
    elif ch == '4':
        allow_deny_port()
    elif ch == '5':
        allow_deny_app()
    elif ch == '6':
        ad_app_lyr_protocol()
    elif ch == '7':
        pass
    else:
        pass

    # allow/deny_rule ends --------------


# ---- active zones
def fw_get_active_zones():
    cmd = 'sudo firewall-cmd --get-active-zones'
    zone = run_cmd(cmd)
    CONF['ZONE'] = zone.split('\n')[0]
    gprint(zone)


# active zone details
@decorate
def fw_get_detail_active_zone():
    fw_get_active_zones()
    cmd = 'ip l'
    gprint(run_cmd(cmd))


# reload
@decorate
def fw_reload():
    cmd = 'sudo firewall-cmd --reload'
    gprint(run_cmd(cmd))


@Error_Handler
def disable_firewall():
    cmd = 'sudo ufw disable'
    gprint(run_cmd(cmd))


def fw_activate():
    gprint('Activating the firewall')
    cmd = 'sudo systemctl start firewalld'
    run_cmd(cmd)


def fw_get_status():
    cmd = 'sudo firewall-cmd --state'
    state = run_cmd(cmd)
    if state == 'running\n':
        gprint('Firewall is active')
    else:
        rprint('Firewall is not active')
        fw_activate()
    fw_get_active_zones()
    gprint('-'*100)


@decorate
def main_menu():
    gprint('[1] Add rules')
    gprint('[2] Delete rules')
    gprint('[3] Allow/Deny firewall rule')
    gprint('[4] Get Active Zones')
    gprint('[5] Get Details of Active Zones')
    gprint('[6] Reload firewall')
    gprint('[7] disable firewall')
    rprint('[8] Exit')


if __name__ == '__main__':
    fw_get_status()
    while True:
        main_menu()
        ch = Prompt.ask('Enter your option : ', choices=[
                        str(x) for x in range(1, 9)])
        if ch == '1':
            # Add rule
            fw_add_rule()
        elif ch == '2':
            # delete rules
            fw_delete_rules()
        elif ch == '3':
            # Allow/Deny rules
            allow_deny_rule()
        elif ch == '4':
            # get active Zones
            fw_get_active_zones()
        elif ch == '5':
            # get active zone details
            fw_get_detail_active_zone()
        elif ch == '6':
            # reload
            fw_reload()
        elif ch == '7':
            disable_firewall()
        elif ch == '8':
            break
        else:
            console.print(
                Text('Wrong option! Type option again ', style='bold red'))
