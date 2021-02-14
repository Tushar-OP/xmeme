
#!/bin/bash


# Any installation related commands
#Install python 3.7
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt  install -y python3.7
#upgrade pip
python3 -m pip install --upgrade pip

#Install requirememts from backend
pip install -r backend/app/requirements.txt