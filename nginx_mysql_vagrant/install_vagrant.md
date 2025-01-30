1) sudo apt update && sudo apt upgrade -y  sudo apt install -y curl gnupg2 software-properties-common

Virtualbox provider fo vagrant : 
2) echo "deb [arch=amd64] https://download.virtualbox.org/virtualbox/debian $(lsb_release -cs) contrib" | sudo tee /etc/apt/sources.list.d/virtualbox.list

2.1) sudo apt-get install dkms build-essential linux-headers-`uname -r`

2.3) sudo /sbin/vboxconfig VBoxManage --version

3) wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -

4) sudo apt update
sudo apt install -y virtualbox-7.0  # Remplacez "7.0" par la dernière version disponible

5) download package Vagrant and install

6) Init vm ubuntu : vagrant init ubuntu/focal64
7) up vm : vagrant up



Permission to avoid rights errors with VirtualBox
1) sudo usermod -aG vboxusers $USER