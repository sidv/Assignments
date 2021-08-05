#!/bin/bash

#group_id=2000
echo "Enter username "
read user
echo "Adding user "$user
sudo useradd $user
echo "Adding new user "$user" with new group" $user
sudo usermod -u 2001 $user
sudo usermod -g 2001 $user
echo "Creating home directory '/home/"$user"'..."
sudo mkdir /home/$user
sudo passwd $user
echo "Changing the user information for "$user
echo "Enter the new value, or press ENTER for the default"
echo "Full Name []:"
read full_name
echo "Room Number []:"
read room_no
echo "Home Phone []:"
read h_phone
echo "Other []:"
read other

sudo usermod -c "$full_name$room_no$h_phone$other" $user
