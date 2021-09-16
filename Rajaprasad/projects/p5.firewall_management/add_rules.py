import pprint
from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text
import os


console = Console()

# ------- add rules start -------

CONF = {}


def get_zone_list():
    cmd = "sudo firewall-cmd --get-zones"
    zone_lst = run_cmd(cmd).split(" ")
    zone_lst[-1] = zone_lst[-1][:-1]
    return zone_lst


def zones():
    zone = Prompt.ask("Enter zone :", choices=get_zone_list(),
                      default=CONF["ZONE"])
    return zone


def gprint(string):
    console.print(Text(string, style="bold green"))


def rprint(string):
    console.print(Text(string, style="bold red"))


def run_cmd(string):
    return os.popen(string).read()


def ports():
    port = Prompt.ask("Enter port number : ")
    return port


def protos():
    proto = Prompt.ask("Enter protocol :", choices=[
        "tcp", "udp"], default="tcp")
    return proto


def fw_add_port():
    cmd = f"sudo firewall-cmd --add-port={ports()}\{protos()} --zone={zones()} --permanent"
    gprint(run_cmd(cmd))
    gprint('-'*100)


def fw_get_services():
    gprint("-"*100)
    gprint("Service List:")
    cmd = "sudo firewall-cmd --get-services"
    gprint(run_cmd(cmd))
    gprint("-"*100)


def fw_add_services():
    fw_get_services()
    service = Prompt.ask("Enter service name from above list : ")
    cmd = f"sudo firewall-cmd --add-service={service} --zone={zones()} --permanent"
    gprint(run_cmd(cmd))
    gprint("-"*100)


def fw_add_sources():
    ip = Prompt.ask('Enter source ip address : ')
    cmd = f'sudo firewall-cmd - -add-source ={ip}'
    gprint(run_cmd(cmd))
    gprint("-"*100)


def fw_add_rule_menu():
    gprint("\t[1]Add Port")
    gprint("\t[2]Add services")
    gprint("\t[3]Add sources")
    rprint("\t[4]Back to Main menu")
    gprint("-"*100)


def fw_add_rule():
    fw_add_rule_menu()
    ch = Prompt.ask("Enter your option : ", choices=["1", "2", "3", "4"])
    if ch == "1":
        # add port
        fw_add_port()
        pass
    elif ch == "2":
        fw_add_services()
        # add services
        pass
    elif ch == "3":
        # add sources
        fw_add_sources()
        pass
    elif ch == "4":
        pass
    else:
        pass


# --------------------add rule ends -------------
