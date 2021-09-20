import paramiko
import time
from rich.console import Console

console = Console()


def cp(string):
    console.print(string, style='bold #00FF00')


def rp(string):
    console.print(string, style='bold red')


# defining error handler decorator
def Error_Handler(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            rp(f'exception flew by! , check credentials and port ')
        else:
            cp('commands executed ....')
        finally:
            cp('execution over !!!!')
    return wrapper


@Error_Handler
def connect(hostname, port, username, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    cp("Connecting.............")
    ssh_client.connect(hostname=hostname, port=port,
                       username=username, password=password)

    return ssh_client


@Error_Handler
def get_shell(ssh_client):
    shell = ssh_client.invoke_shell()
    return shell


@Error_Handler
def send_cmd(shell, cmd):
    cp(f"Sending...{cmd}")
    shell.send(cmd+"\n")
    time.sleep(1)


@Error_Handler
def show(shell):
    output = shell.recv(10000)
    return output.decode()


@Error_Handler
def close(ssh_client):
    if ssh_client.get_transport().is_active() == True:
        cp("Disconnecting.............")
        ssh_client.close()


if __name__ == "__main__":
    client = connect("192.168.1.11", 22, "raja", "raja1234")
    shell = get_shell(client)

    send_cmd(shell, "ls")
    send_cmd(shell, "df")
    send_cmd(shell, "free -m")
    send_cmd(shell, "w")
    send_cmd(shell, "sudo route -n")
    send_cmd(shell, "uptime")

    output = show(shell)
    cp(output)
