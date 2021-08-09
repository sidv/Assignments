#!/bin/bash

echo "Enter a UserName"
read uname
echo "Adding User"
sudo useradd $uname
echo "Adding userid(2001)"
sudo usermod -u 2001 $uname
echo "Adding groupid(1000)"
sudo usermod -g 1000 $uname
echo "Adding user to the sudo group"
sudo usermod -G sudo $uname
echo "Creating home direcctory for user"
sudo mkdir "/home/"$uname
echo "Updating password for the user"
sudo passwd $uname
echo "Changing user information"
echo "Enter your name"
read name
sudo usermod -c $name $uname
