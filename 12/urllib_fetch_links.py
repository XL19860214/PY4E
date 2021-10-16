# Copyright (c) Xuwei Li

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# User inputs
inputUrl = input('Enter URL:')
if len(inputUrl) < 1:
    inputUrl = 'http://py4e-data.dr-chuck.net/known_by_Insiya.html'
    print('Use default URL: ', inputUrl)

inputCount = input('Enter count:')
if len(inputCount) < 1:
    countValue = 7
    print('Use default count: ', countValue)
else:
    countValue = int(inputCount)

inputPosition = input('Enter position:')
if len(inputPosition) < 1:
    positionValue = 18
    print('Use default position: ', positionValue)
else:
    positionValue = int(inputPosition)

# Fetch page
def fetchLink(url, pos):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    link = tags[pos]
    newUrl = link.get('href')
    print('Retrieving:', link.get('href'))
    return newUrl

# Loop according to user input
url = inputUrl
i = 0
while i < countValue:
    url = fetchLink(url, positionValue - 1)
    i += 1
