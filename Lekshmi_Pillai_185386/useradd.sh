
#!/bin/bash

read  user
sudo useradd -u 2003 $user
sudo passwd $user
sudo groupadd monitorlekshmi
sudo usermod -G  monitorlekshmi $user
echo "Enter Your Name"
read name
sudo usermod -c $name $user
