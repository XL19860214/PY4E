# Copyright (c) Xuwei Li

import urllib.request
import json
import ssl

# User input
inputUrl = input('Enter location:')
if len(inputUrl) < 1:
    inputUrl = 'http://py4e-data.dr-chuck.net/comments_1362839.json'
    print('Use default URL:', inputUrl)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Open Url & Process data
urlHandle = urllib.request.urlopen(inputUrl, context=ctx)
data = urlHandle.read()
print('Retrieved', len(data), 'characters')
jsonObj = json.loads(data)

print('Count:', len(jsonObj['comments']))

## Sum
sum = 0
for comment in jsonObj['comments']:
    sum += int(comment['count'])

print('Sum:', sum)
