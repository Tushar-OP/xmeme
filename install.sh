
#!/bin/bash


# Any installation related commands
#Install python 3.7
sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt update
sudo apt  install -y python3.7
sudo apt install -y python3-pip
#upgrade pip
python3 -m pip install --upgrade pip

#Install requirememts from backend
pip3 install -r backend/app/requirements.txt
