#!/bin/bash 

sudo apt update;
sudo apt dist-upgrade;

curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
