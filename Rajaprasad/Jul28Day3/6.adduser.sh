#!/bin/bash

echo "Enter username"
read user

echo "adding user"

sudo useradd $user

echo "adding user group "
 
sudo usermod -G shanu $user

echo "adding user uid (2008)"

sudo usermod -u 2008 $user



echo "adding user gid =(1001) "
sudo usermod -g 1001 $user

echo "creating home directory "

sudo mkdir "/home/"$user

echo  "creating password"

sudo passwd $user

echo "enter your name"

read name


echo "adding user group" 






