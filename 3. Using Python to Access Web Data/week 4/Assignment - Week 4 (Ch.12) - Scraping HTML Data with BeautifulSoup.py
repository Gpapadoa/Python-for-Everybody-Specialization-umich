# Using Python to Access Web Data - University of Michigan

# Assignment - Week 4 (Ch.12): Scraping HTML Data with BeautifulSoup
# open url, count and sum

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

count = 0
itags = list()

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag:
    # print('span:', tag)
    # print('Contents:', tag.contents[0])
    count += 1 #count = count +1
    itags.append ( int(tag.contents[0]) ) # string to integer


sum_tags = sum(itags)

print('There are,',count,'values with a sum =',sum_tags)
out = input('Press enter to exit')

# Sum: 2445 (http://py4e-data.dr-chuck.net/comments_1054993.html)




