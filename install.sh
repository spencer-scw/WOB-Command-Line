#!/bin/bash

apt install python3-pip
pip install bs4 requests

chmod 755 wob api-wrapper.py

cp -p wob api-wrapper.py /bin