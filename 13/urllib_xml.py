# Copyright (c) Xuwei Li

import urllib.request
import xml.etree.ElementTree as ET
import ssl

# User input
inputUrl = input('Enter location:')
if len(inputUrl) < 1:
    inputUrl = 'http://py4e-data.dr-chuck.net/comments_1362838.xml'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Open Url & Process data
urlHandle = urllib.request.urlopen(inputUrl, context=ctx)
data = urlHandle.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
counts = tree.findall('.//count')
print('Count:', len(counts))

# Sum
sum = 0
for count in counts:
    sum += int(count.text)

print('Sum:', sum)
