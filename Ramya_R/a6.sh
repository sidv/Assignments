#! /bin/bash

echo "Enter uname"
read user
echo "add user"
sudo adduser $user
echo "add user with uid 2000"
sudo usermod -u 2000 $user
echo "add user with gid 2008"
sudo usermod -g 2008 $user
echo "add user to group"
sudo usermod -G sudo $user
echo "creating home dir"
sudo mkdir "/home/"$user
sudo passwd $user
echo "enter full name"
read name
#sudo usermod -c $name $user
#echo "Enter address"
#read add

