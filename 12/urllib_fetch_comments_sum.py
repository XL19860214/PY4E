# Copyright (c) Xuwei Li

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

inputUrl = input('Enter URL:')
if len(inputUrl) < 1:
    inputUrl = 'http://py4e-data.dr-chuck.net/comments_1362836.html'

html = urlopen(inputUrl, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the span.comments tags
tags = soup('span', { 'class': 'comments' })
sum = 0
for tag in tags:
    sum += int(tag.text)

print(sum)
