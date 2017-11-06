#!/usr/bin/env python

from google import search
import random
import time
import requests
 
queries = ['kali as a regular os', 'which martial art to learn', 'how to think like a baby', 'deadliest martial arts']

while(True):
    query = random.choice(queries)
    print query

    for j in search(query, tld="com", lang="en", num=10, stop=1, pause=4):
        # if 'rafed123.github.io' in j:
        print j
