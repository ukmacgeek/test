#!/usr/bin/python

# Import Libraries
import json
import urllib2
import time

# Enter postcode from command line
postcode = raw_input('Please provide your postcode : ').lower()
postcode = postcode.replace(' ','')

#make sure we take out all spaces and special characters
if not postcode.isalnum():
   print 'Please provide the postcode with no spaces or special characters'
   exit()
# Pull code to get API Key from file

# Start getting data from google maps based on postcode
locationUrl = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + postcode + '&key=<enter API key here>'
locationResponse = urllib2.urlopen(locationUrl)
locationResult = json.loads(locationResponse.read())
locationResult2 = locationResult['results']

# Get address from google data
address = locationResult2[0]['formatted_address']

# Get longs and lats from google data
myLocation = locationResult2[0]['geometry']['location']
myLat = str(myLocation['lat'])
myLong = str(myLocation['lng'])

# Now get ISS data passing in lat and long from google geo location data
issUrl = 'http://api.open-notify.org/iss-pass.json?lat=' + myLat + '&lon=' + myLong
issResponse = urllib2.urlopen(issUrl)
issResult = json.loads(issResponse.read())

# get the first (0) time from ISS response and convert to a real time from 1 Jan 1970
isstime = issResult['response'][0]['risetime']
nexttime = time.ctime(isstime)

# Now print out the information of the next time the ISS will pass over the postcode.
print 'At ' + nexttime + ' the ISS will pass overhead ' + address
exit()

