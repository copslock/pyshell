#!/usr/bin/python


import os
import requests


url = ''
fileName = ''
req = requests.get(url)
file = open(fileName, 'wb')
for chunk in req.iter_content(100000):
    file.write(chunk)
file.close()
