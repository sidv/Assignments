#!/bin/bash
echo "enter name of user"
read user

echo "Adding user "$user" ..."
sudo useradd $user
echo "Adding new group "$user" (1006) ..."
sudo usermod -u 1006 $user
echo "Adding new user "$user" (1006) with group" $user" ..."
sudo usermod -g 1006 $user
echo "Creating home directory /home/"$user
sudo mkdir "/home/"$user
sudo passwd $user 
echo "Changing the user information for "$user
echo "Full Name []:" read name
 
echo "Room Number []: "
	"Work Phone []: "
	"Home Phone []: "
