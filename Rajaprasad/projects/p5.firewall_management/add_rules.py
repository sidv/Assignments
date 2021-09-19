
from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text
import os


console = Console()

# ------- add rules start -------


# defining error handler decorator
def Error_Handler(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            rprint(f'exception flew by! , {func.__name__} use sudo instead ')
        else:
            gprint('commands executed ....')
        finally:
            gprint('execution over !!!!')
    return wrapper


CONF = {}


def get_zone_list():
    cmd = 'sudo firewall-cmd --get-zones'
    zone_lst = run_cmd(cmd).split(' ')
    zone_lst[-1] = zone_lst[-1][:-1]
    return zone_lst


def zones():
    zone = Prompt.ask('Enter zone :', choices=get_zone_list(),
                      default=CONF['ZONE'])
    return zone


def gprint(string):
    console.print(Text(string, style='bold green'))


def rprint(string):
    console.print(Text(string, style='bold red'))


# define decorator
def decorate(func):

    def wrap_func():
        gprint('*'*100)
        func()
        gprint('*'*100)

    return wrap_func


def run_cmd(string):
    return os.popen(string).read()


def ports():
    port = Prompt.ask('Enter port number : ')
    return port


def protos():
    proto = Prompt.ask('Enter protocol :', choices=[
        'tcp', 'udp'], default='tcp')
    return proto


def allow_deny():
    alw_dny = Prompt.ask('Enter option : ', choices=[
                         'allow', 'deny'], default='allow')
    return alw_dny


def interface_choice():
    s = os.popen(
        'ip l | cut -d":" -f2 | tr -d ' ' | cut -d' ' -f1').read()
    interfaces = s.split('\n')[:-2:2]
    interface_choice = Prompt.ask(
        'Enter Interface : ', choices=interfaces, default='enp0s3')
    return interface_choice


def ip_addr():
    ip = Prompt.ask('Enter Host/ip : ')
    if len(ip.split('.')) == 4:
        return ip


@Error_Handler
def fw_add_port():
    cmd = f'sudo firewall-cmd --add-port={ports()}/{protos()} --zone={zones()} --permanent'
    gprint(run_cmd(cmd))


@decorate
def fw_get_services():
    gprint('Service List:')
    cmd = 'sudo firewall-cmd --get-services'
    gprint(run_cmd(cmd))


@Error_Handler
def fw_add_services():
    fw_get_services()
    service = Prompt.ask('Enter service name from above list : ')
    cmd = f'sudo firewall-cmd --add-service={service} --zone={zones()} --permanent'
    gprint(run_cmd(cmd))


@Error_Handler
def fw_add_sources():
    ip = Prompt.ask('Enter source ip address : ')
    cmd = f'sudo firewall-cmd - -add-source ={ip}'
    gprint(run_cmd(cmd))


@decorate
def fw_add_rule_menu():
    gprint('\t[1]Add Port')
    gprint('\t[2]Add services')
    gprint('\t[3]Add sources')
    rprint('\t[4]Back to Main menu')


def fw_add_rule():
    fw_add_rule_menu()
    ch = Prompt.ask('Enter choice : ', choices=[
                    str(x) for x in range(1, 5)], default='1')
    if ch == '1':
        # add port
        fw_add_port()
    elif ch == '2':
        # add services
        fw_add_services()
    elif ch == '3':
        # add sources
        fw_add_sources()
    elif ch == '4':
        pass
    else:
        pass

# --------------------add rule ends -------------
