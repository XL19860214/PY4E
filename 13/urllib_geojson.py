# Copyright (c) Xuwei Li

import urllib.request, urllib.parse
import json
import ssl

# API Endpoint
serviceUrl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# User input
inputLocation = input('Enter location:')
if len(inputLocation) < 1:
    inputLocation = 'University of Buenos Aires'
    print('Use default location:', inputLocation)
url = serviceUrl + urllib.parse.urlencode({ 'key': '42', 'address': inputLocation })

# Open URL & Process
print('Retrieving', url)
urlHandle = urllib.request.urlopen(url, context=ctx)
data = urlHandle.read().decode()
print('Retrieved', len(data), 'characters')
try:
    js = json.loads(data)
except:
    js = None

print('Place id', js['results'][0]['place_id'])
