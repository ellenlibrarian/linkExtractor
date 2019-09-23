# This script goes to a website and grabs the anchor tag href and name. It filters to remove links that do not begin with the library proxy prefix. It writes the name (or None, if not available) and URL to a file.
# I wrote this to quickly grap database names and URLs from the library website for link testing purposes (finding links that were redirecting, etc.)
# requires urlib, BeautifulSoup, ssl

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

fout = open("output/web-href-tags3.txt", "w")

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Prompt for the URL and parse the page
url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # grab the href attribute
    url = tag.get('href', None)
    print(url)
    # filter out non-proxied links
    if not url.startswith("https://libproxy.usouthal.edu/login?url=http://") : # change this root URL according to the purpose
        continue
    # get the title attribute
    title = tag.get('title', None)
    print(title)
    # write to text file
    fout.write(str(title) + "\n" + str(url) + "\n\n" )
