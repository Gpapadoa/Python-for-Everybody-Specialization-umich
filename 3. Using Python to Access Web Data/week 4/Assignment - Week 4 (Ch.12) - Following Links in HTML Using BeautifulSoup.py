# Using Python to Access Web Data - University of Michigan

# Assignment - Week 4 (Ch.12): Following Links in HTML Using BeautifulSoup
# open url and find

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int ( input('Enter count: ',) )
position = int( input('Enter position: ',) )
names = list()

for x in range(count):

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    if x == 0: print('Retrieving:',url)

    # Retrieve all of the anchor tags
    tags = soup('a')
    i_count = 0

    for tag in tags:
        # print(tag.get('href', None))
        i_count +=1
        if i_count == position:
            url = tag.get('href', None)
            names.append(tag.contents[0])
            # print(url)
            break

    print('Retrieving:',url)

print(names)
out = input('Press enter to exit')

# ['Anis', 'Rybecca', 'Liam', 'Charlie', 'Ferne', 'Izabella', 'Palmer'] -  http://py4e-data.dr-chuck.net/known_by_Kayley.html
# count: 7 , position: 18 

    
