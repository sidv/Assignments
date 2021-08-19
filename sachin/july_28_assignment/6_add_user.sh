#!/bin/bash

echo "Enter username"
read user

echo "adding user"

sudo useradd $user

echo "adding user group "
 
sudo usermod -G sachin $user

echo "adding user uid (2001) "

sudo usermod -u 2001 $user



echo "adding user gid =(1000) "
sudo usermod -g 1000 $user

echo "creating home directory "

sudo mkdir "/home/"$user

echo  "creating password"

sudo passwd $user

echo "enter your name"

read name


echo "adding user group " 






