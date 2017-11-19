#!/usr/bin/python

import json
import urllib2
import time

url = 'http://api.open-notify.org/astros.json'
response = urllib2.urlopen(url)

result = json.loads(response.read())

#print result

print 'people in space: ' , result['number']

people = result['people']

#print people

for p in people:
   print p['name'] + ', on : ' + p['craft']
