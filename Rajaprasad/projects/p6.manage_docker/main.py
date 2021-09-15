#!/usr/bin/python3
import os
from rich.text import Text
from rich.console import Console
import json


console = Console()


def cp(string):
    console.print(Text(string, style='bold #00FF00'))


def run_cmd(str):
    return os.popen(str).read()


def main_menu():
    cp('-'*20)
    cp('1.Status of containers')
    cp('2.Download new Image')
    cp('3.Run container')
    cp('4.Delete Container')
    cp('5.Network details of container')
    cp('6.Modify Network details of contaniner')
    cp('7.Exit')
    cp('-'*20)


while True:
    main_menu()
    ch = int(input("Enter choice : "))
    if ch == 1:
        # checking docker container status
        cmd = 'docker container stats'
        os.system(cmd)
    elif ch == 2:
        # download images from docker repo
        image_nm_tag = input("Enter image_name:tag ")
        cmd = f'docker pull {image_nm_tag}'
        cp(run_cmd(cmd))
    elif ch == 3:
        # run container
        image_nm_tag = input("Enter image_name:tag ")
        container_name = input('Enter container name ')
        cmd = f'docker run --name {container_name} {image_nm_tag}'
        cp(run_cmd(cmd))
        cmd2 = 'docker ps -a |head -n 2'
        cp(run_cmd(cmd2))

    elif ch == 4:
        # delete container
        container_name = input('Enter container name ')
        cmd = f'docker rm {container_name}'
        cp(f'{run_cmd(cmd)} container deleted successfully ')
    elif ch == 5:
        # network details of a container
        cmd = 'docker network inspect bridge'
        l = run_cmd(cmd)
        l = json.loads(l)[0]
        for i in l["Containers"].values():
            cp(
                f'Name => {i["Name"]} | Mac address => {i["MacAddress"]} | ipv4 address =>{i["IPv4Address"]}')
    elif ch == 6:
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

    elif ch == 7:
        break

    else:
        console.print('Wrong option ', style='bold red')
