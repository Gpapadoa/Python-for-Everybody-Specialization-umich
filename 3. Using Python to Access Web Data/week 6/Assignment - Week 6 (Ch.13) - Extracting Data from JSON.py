# Using Python to Access Web Data - University of Michigan

# Assignment - Week 6 (Ch.13): Extracting Data from JSON

import urllib.request, urllib.parse, urllib.error
import json

while True:

    #Data collection
    address = input('Enter location or enter to exit: ')
    print('Retrieving', address)

    data = urllib.request.urlopen(address).read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    # uncomment line 19 to see the data
    # print ( js )

    cn = 0 #count
    sm = 0 #sum

    # js is a dic and with the key:'comments' we get the value which is a list of dicts
    # and item in for-loop is every dict in that list. 
    # then with the key:'count' in every-dict (item) inside that list we get the value we want to make the sum

    for item in js['comments']: 
        cn += 1
        i_value = int(item['count'])
        sm += i_value

    print('Count:', cn)
    print('Sum:', sm)