#!/usr/bin/python

import json
import urllib2

url = 'https://httpbin.org/get'
response = urllib2.urlopen(url)
result = json.loads(response.read())

print 'origin information ' + result['origin']

headerResult = result['headers']

print headerResult

print 'header agent ' + headerResult['User-Agent']

