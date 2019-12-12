#!/bin/bash

#update and install required packages
apt-get update -y && apt-get install python3 python3-dev python3-pip git -y

#clone the repository and process the script further
git clone https://github.com/rahul1809/Scripts.git

cd Scripts/Google-Colab/

#install the required packages
pip install -r requirements.txt

cd -

rm -rf Scripts/

