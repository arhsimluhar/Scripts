#!/bin/bash

#update and install required packages
apt-get update -y && apt-get install python3 pythom3-dev python3-pip -y && pip install -r requirements.txt

