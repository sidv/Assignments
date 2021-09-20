#!/usr/bin/python3
import os
from rich.text import Text
from rich.console import Console
from rich.prompt import Prompt
import json


console = Console()


def cp(string):
    console.print(Text(string, style='bold #00FF00'))


def rp(string):
    console.print(Text(string, style='bold red'))


def run_cmd(str):
    return os.popen(str).read()


# defining error handler decorator
def Error_Handler(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            rp(f'exception flew by! , {func.__name__} use sudo instead ')
        else:
            cp('commands executed ....')
        finally:
            cp('execution over !!!!')
    return wrapper


# define decorator
def decorate(func):

    def wrap_func():
        cp('*'*100)
        func()
        cp('*'*100)

    return wrap_func


@decorate
def main_menu():
    cp('[1].Status of containers')
    cp('[2].Download new Image')
    cp('[3].Run container')
    cp('[4].Delete Container')
    cp('[5].Network details of container')
    cp('[6].Modify Network details of contaniner')
    rp('[7].Exit')


@Error_Handler
def docker_cn_status():
    # checking docker container status
    cmd = 'docker container stats'
    os.system(cmd)


@Error_Handler
def docker_dwn_image():
    # download images from docker repo
    image_nm_tag = input("Enter image_name:tag ")
    cmd = f'docker pull {image_nm_tag}'
    cp(run_cmd(cmd))


@Error_Handler
def run_container():
    # run container
    image_nm_tag = input("Enter image_name:tag ")
    container_name = input('Enter container name ')
    cmd = f'docker run --name {container_name} {image_nm_tag}'
    cp(run_cmd(cmd))
    cmd2 = 'docker ps -a |head -n 2'
    cp(run_cmd(cmd2))


@Error_Handler
def delete_container():
    # delete container
    container_name = input('Enter container name ')
    cmd = f'docker rm {container_name}'
    cp(f'{run_cmd(cmd)} container deleted successfully ')


@Error_Handler
def network_detail_container():
    # network details of a container
    cmd = 'docker network inspect bridge'
    l = run_cmd(cmd)
    l = json.loads(l)[0]
    for i in l["Containers"].values():
        cp(
            f'Name => {i["Name"]} | Mac address => {i["MacAddress"]} | ipv4 address =>{i["IPv4Address"]}')


@Error_Handler
def docker_modify_network():
    container_name = input(
        'Enter container name for disconnect from bridge network : ')
    cmd = f'docker network disconnect bridge {container_name}'
    run_cmd(cmd)
    cp(
        f'{container_name} container disconnect from bridge network')

    cp('creating network')
    network = input(
        'enter a new network name  for docker network creation : ')
    cmd2 = f' sudo docker network create -d bridge --subnet=192.168.1.0/24  {network}'
    run_cmd(cmd2)
    print(f'{network} Network created successfully')

    cp(
        'connect our container to newly created network')
    ntwork = input('Enter newly created network name :')
    cmd3 = f'docker network connect {ntwork} {container_name}'
    run_cmd(cmd3)
    cp(
        f'{container_name} container connected to {ntwork} Network')


def Exit():
    exit()


operations = {
    '1': docker_cn_status,
    '2': docker_dwn_image,
    '3': run_container,
    '4': delete_container,
    '5': network_detail_container,
    '6': docker_modify_network,
    '7': Exit
}

while True:
    main_menu()
    ch = Prompt.ask('Enter choice ', choices=[
                    str(x) for x in range(1, 8)], default='1')
    operations[ch]()
