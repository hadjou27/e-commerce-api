# Django Rest API


## Installation

- `sudo apt upgrade` : to update the OS
- `sudo apt install -y -ce docker`
- `docker-compose build` to build the image 

## Installing Docker in a Linux environment
Here are the steps to install Docker in WSL:

Update package info:

sudo apt update

Install prerequisites:

sudo apt install -y apt-transport-https ca-certificates curl software-properties-common

Add Docker's GPG key:

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

Add Docker repository:

`echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list`

Update packages again and install Docker:

`sudo apt update`
`sudo apt install -y docker-ce docker-ce-cli containerd.io`

Start Docker service:

`sudo service docker start`

Add your user to docker group to run without sudo:

`sudo usermod -aG docker $USER`
Log out and back in for group changes to take effect.


