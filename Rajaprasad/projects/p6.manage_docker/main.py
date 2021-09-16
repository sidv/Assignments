#!/usr/bin/python3
import os
from rich.prompt import Prompt
from rich import style
from rich.console import Console
import json


console = Console()


def main_menu():
    console.print('-'*20, style='bold #00FF00')
    console.print('1.Status of containers', style='bold #00FF00')
    console.print('2.Download new Image', style='bold #00FF00')
    console.print('3.Run container', style='bold #00FF00')
    console.print('4.Delete Container', style='bold #00FF00')
    console.print('5.Network details of container', style='bold #00FF00')
    console.print('6.Modify Network details of contaniner',
                  style='bold #00FF00')
    console.print('7.Exit', style='bold #00FF00')
    console.print('-'*20, style='bold #00FF00')


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
        res = os.popen(cmd).read()
        console.print(res, style='bold italic green')
    elif ch == 3:
        # run container
        image_nm_tag = input("Enter image_name:tag ")
        container_name = input('Enter container name ')
        cmd = f'docker run --name {container_name} {image_nm_tag}'
        os.system(cmd)
        console.print(os.popen('docker ps -a |head -n 2').read(),
                      style='bold italic yellow')

    elif ch == 4:
        # delete container
        container_name = input('Enter container name ')
        cmd = f'docker rm {container_name}'
        res = os.popen(cmd).read()
        console.print(f'{res} container deleted successfully ',
                      style='bold italic yellow')
    elif ch == 5:
        # network details of a container
        cmd = 'docker network inspect bridge'
        l = os.popen(cmd).read()
        l = json.loads(l)[0]
        for i in l["Containers"].values():
            console.print(
                f'Name => {i["Name"]} | Mac address => {i["MacAddress"]} | ipv4 address =>{i["IPv4Address"]}', style='bold italic green')
    elif ch == 6:
        container_name = input(
            'Enter container name for disconnect from bridge network : ')
        cmd = f'docker network disconnect bridge {container_name}'
        print(os.popen(cmd).read())
        console.print(
            f'{container_name} container disconnect from bridge network', style='bold green')

        console.print('creating network', style='bold red')
        network = input(
            'enter a new network name  for docker network creation : ')
        cmd2 = f' sudo docker network create -d bridge --subnet=192.168.1.0/24  {network}'
        print(os.popen(cmd2).read())
        print(f'{network} Network created successfully')

        console.print(
            'connect our container to newly created network', style='bold red')
        ntwork = input('Enter newly created network name :')
        cmd3 = f'docker network connect {ntwork} {container_name}'
        print(os.popen(cmd3).read())
        console.print(
            f'{container_name} container connected to {ntwork} Network', style='bold green')

    elif ch == 7:
        break

    else:
        console.print('Wrong option ', style='bold red')
