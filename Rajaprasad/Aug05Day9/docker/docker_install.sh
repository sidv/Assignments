#!/bin/bash

echo "Installing docker ............."

echo "Uninstalling docker old versions......."
sudo apt-get remove docker docker-engine docker.io containerd runc

echo "Update the apt package index and install packages to allow apt to use a repository over HTTPS:"
sudo apt-get update
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
echo "Add Docker’s official GPG key:"
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo "set up the stable repository and it's detect your linux version automatically "
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

echo "Updating the apt package index"
sudo apt-get update

echo "installing the latest version of Docker Engine and containerd"
sudo apt-get install docker-ce docker-ce-cli containerd.io
