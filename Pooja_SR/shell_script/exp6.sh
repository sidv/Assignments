#!/bin/bash

echo "Enter name of new user"
read user
echo "Adding the userto a group"
sudo useadd $user
echo "adding the uid is 2001"
sudo usermod -u 2001 $user
echo "adding the gid is 1000"
sudo usermod -g 1000 $user
echo "Adding the userto sudo group"
sudo usermod -G sudo $user
echo "creating home directory"
sudo mkdir "/home/"$user

sudo passwd -c  $user
echo "change info"
echo "enteryour name"
read name
sudo usermod -c name $user
echo "enter your address"
read address
sudo usermod -c address $user
