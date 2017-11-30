#!/usr/bin/python



import urllib
import urllib2
import json
import time
import requests
import datetime



# def hiveurlrequest(inurl, data, sessionid, type):
#     opener = urllib2.build_opener(urllib2.HTTPHandler)
#     if data:
#         request = urllib2.Request(inurl, data=data)
#     else:
#         request = urllib2.Request(inurl)
#
#     request.add_header("Content-Type", 'application/vnd.alertme.zoo-6.5.0+json')
#     request.add_header("Accept", 'application/vnd.alertme.zoo-6.5.0+json')
#     request.add_header("X-Omnia-Client", 'Hive Web Dashboard')
#     request.add_header("X-Omnia-Access-Token", sessionid)
#     request.get_method = lambda: type
#     opener.open(request)

username = raw_input('Enter Username :')
password = raw_input('Password :')
url = 'https://api-prod.bgchprod.info:443/omnia'

loginUrl = url + '/auth/sessions'
data = {'username': username, 'password': password}
datal2 = {'sessions': [data]}
jsonData = json.dumps(datal2)

loginRequest = urllib2.Request(loginUrl, data=jsonData)
loginRequest.add_header("Content-Type",'application/vnd.alertme.zoo-6.1+json')
loginRequest.add_header("Accept",'application/vnd.alertme.zoo-6.1+json')
loginRequest.add_header("X-Omnia-Client",'Hive Web Dashboard')

try:
    loginResponse = urllib2.urlopen(loginRequest)
except urllib2.HTTPError, error:
    loginResponse = error

if loginResponse.code != 200:
    loginResponseCode = str(loginResponse.code)
    print 'Failed to connect to Hive error code ' + loginResponseCode
    exit()
else:
    sessionData = loginResponse.read()
    sessionId = json.loads(sessionData)['sessions'][0]['sessionId']

deviceUrl = url + '/nodes'
deviceRequest = urllib2.Request(deviceUrl)
hiveHeaders = {'Content-Type': 'application/vnd.alertme.zoo-6.5.0+json','Accept':'application/vnd.alertme.zoo-6.5.0+json','X-Omnia-Client':'Hive Web Dashboard','X-Omnia-Access-Token': sessionId}
try:
    deviceData = requests.get(deviceUrl, headers = hiveHeaders)
except requests.HTTPError, error:
    deviceData = error

if deviceData.status_code != 200:
    deviceDataCode = str(deviceData.status_code)
    print 'Failed to connect to Hive error code ' + deviceDataCode
    exit ()
else:
    devices = json.loads(deviceData.content)

print devices

# deviceRequest.add_header("Content-Type", 'application/vnd.alertme.zoo-6.5.0+json')
# deviceRequest.add_header("Accept", 'application/vnd.alertme.zoo-6.5.0+json')
# deviceRequest.add_header("X-Omnia-Client", 'Hive Web Dashboard')
# deviceRequest.add_header("X-Omnia-Access-Token", sessionId)
#
# try:
#     deviceResponse = urllib2.urlopen(deviceRequest)
# except urllib2.HTTPError, error:
#     deviceResponse = error
#
# if deviceResponse.code != 200:
#     deviceResponseCode = str(deviceResponse.code)
#     print 'Failed to connect to Hive error code ' + deviceResponseCode
#     exit()
# else:
#     deviceData = deviceResponse.read()
#     devices = json.loads(deviceData)
    #print devices

#print devices['nodes'][1]['features']['on_off_device_v1']['mode']['displayValue']

for nodes in devices['nodes']:
    try:
        firstInst = nodes['firstInstall']
        firstInstall = time.ctime(firstInst)
    except KeyError:
        firstInstall = ''

    try:
        temp = nodes['features']['temperature_sensor_v1']['temperature']['reportedValue']
        tempInfo = ' Current Temp is ' + str(temp)
    except KeyError:
        tempInfo = ''

    try:
        on_off = nodes['features']['on_off_device_v1']['mode']['displayValue']
        on_offInfo = ' is ' + on_off
    except KeyError:
        on_offInfo = ''

    if firstInstall:
        print 'node name = ' + nodes['name'] + ' ' + on_offInfo + tempInfo

        # nodeId = nodes['id']
        # nodeUrl = url + '/nodes/' + nodeId
        # nodeRequest = urllib2.Request(nodeUrl)
        # nodeRequest.add_header("Content-Type", 'application/vnd.alertme.zoo-6.5.0+json')
        # nodeRequest.add_header("Accept", 'application/vnd.alertme.zoo-6.5.0+json')
        # nodeRequest.add_header("X-Omnia-Client", 'Hive Web Dashboard')
        # nodeRequest.add_header("X-Omnia-Access-Token", sessionId)
        #
        # try:
        #     nodeResponse = urllib2.urlopen(nodeRequest)
        # except urllib2.HTTPError, error:
        #     nodeResponse = error
        #
        # if nodeResponse.code != 200:
        #     nodeResponseCode = str(nodeResponse.code)
        #     print 'Failed to connect to Hive error code ' + nodeResponseCode
        #     exit()
        # else:
        #     nodeData = nodeResponse.read()
        #     node = json.loads(nodeData)
        #
        # print node


# adeviceUrl = url + '/nodes/882207e1-7842-49b0-8d09-8c4e7ec30631'
# adeviceRequest = urllib2.Request(adeviceUrl)
# adeviceRequest.add_header("Content-Type", 'application/vnd.alertme.zoo-6.5.0+json')
# adeviceRequest.add_header("Accept", 'application/vnd.alertme.zoo-6.5.0+json')
# adeviceRequest.add_header("X-Omnia-Client", 'Hive Web Dashboard')
# adeviceRequest.add_header("X-Omnia-Access-Token", sessionId)
#
# try:
#     adeviceResponse = urllib2.urlopen(adeviceRequest)
# except urllib2.HTTPError, error:
#     adeviceResponse = error
#
# if adeviceResponse.code != 200:
#     adeviceResponseCode = str(adeviceResponse.code)
#     print 'Failed to connect to Hive error code ' + adeviceResponseCode
#     exit()
# else:
#     adeviceData = adeviceResponse.read()
#     adevices = json.loads(adeviceData)
#     print adevices

def light(status):
    ondata = {'nodes': [{'features': {'on_off_device_v1': {'mode': {'targetValue': status}}}}]}
    jsonondata = json.dumps(ondata)
    onurl = url + '/nodes/13433e4f-6dae-48fe-aee3-fc968d58f7b1'
    requests.put(onurl, headers = hiveHeaders, data = jsonondata)

#light('OFF')
sunriseUrl = 'https://api.sunrise-sunset.org/json?lat=55.922059&lng=-4.4474665'
sunrisesunset = requests.get(sunriseUrl)
sunrise = json.loads(sunrisesunset.content)
nowdate = datetime.datetime.now()
sunrisetime = time.strptime(nowdate.strftime('%Y/%m/%d') + sunrise['results']['sunrise'],'%Y/%m/%d%I:%M:%S %p')
#print sunrisetime , time.localtime() #time.strptime(time.localtime(),'%d/%m/%Y')
if sunrisetime < time.localtime():
    nowdate = datetime.datetime.now() + datetime.timedelta(days=1)
    sunrisetime = time.strptime(nowdate.strftime('%Y/%m/%d') + sunrise['results']['sunrise'],'%Y/%m/%d%I:%M:%S %p')

# while time.localtime() < sunrisetime:
#     time.sleep(30)
#     print 'waiting for ' + str(sunrisetime)

light('OFF')