#!/usr/bin/env python

import requests
import time
from stem import Signal
from stem.control import Controller

################### CONFIG ######################
# heroes
reza = 306
biplob = 450

url = 'http://campaign.thedailystar.net/teachersday/setlike'
data={
    'id': reza
}
headers={
    'Referer': 'http://campaign.thedailystar.net/teachersday'
}
################### CONFIG ######################

# def newSession():
#     session = requests.session()
#     session.proxies = {'http':  'socks5://127.0.0.1:9050',
#                        'https': 'socks5://127.0.0.1:9050'}
#     return session

proxy = {'http':  'socks5://127.0.0.1:9050',
         'https': 'socks5://127.0.0.1:9050'}

def newConn(): # tor connection
    with Controller.from_port(port = 9051) as controller: # edit /etc/torrc -> uncomment ControlPort 9051
        controller.authenticate(password="password")
        controller.signal(Signal.NEWNYM)

for i in range(100):
    print '[*] Changing IP...'
    newConn()
    
    print '[*] Sending request...'
    response = requests.post(url, data=data, headers=headers, proxies=proxy)
    print '[+] Server sent:', response.text

    time.sleep(6)

