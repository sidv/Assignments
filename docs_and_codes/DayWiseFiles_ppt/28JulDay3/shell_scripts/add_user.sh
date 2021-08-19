#!/bin/bash


echo "Enter username"
read user
echo "Adding user"
echo "Adding user group"
sudo useradd $user
echo "Adding user uid(2001)"
sudo usermod -u 2001 $user
echo "Adding user gid(1000)"
sudo usermod -g 1000 $user
echo "Adding user to sudo group"
sudo usermod -G  sudo $user
echo "Creating home directory"
sudo mkdir "/home/"$user
sudo passwd $user
echo "Changing user information"
echo "Enter your name"
read name
sudo usermod -c $name $user
echo "Enter address"
read address
sudo usermod -c $address $user
