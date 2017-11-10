#!/usr/bin/env python3

# Luis Chunga
# Project 5
# Doc string description of project
"""
This program will perform a simple web scraping.  Python modules
(requests, bs4 as in 'BeautifulSoup') will be imported to retrieve
and process data. The program will sometimes need to use the google
maps api to compute distances between cities. A sample test using
google maps api can be done in a browser by visiting a website.
For example, "https://maps.googleapis.com/maps/api/distancematrix/json?
origins=murfreesboro,tn&destinations=nashville,tn" to check the
distance between Murfreesboro, TN and Nashville, TN.

The program will be invokable in 3 different ways:
    python3 ./p5.py -x city1,state1 city2,state2
    python3 ./p5.py -j city1,state1 city2,state2
    python3 ./p5.py -a some_url

If the -j option is used, then the google distancematrix site will
be used requesting json output.  If the -x is used, then the same site
will be used, but requesting xml instead.  When json is requested, it
will be processed by methods available in the requests module.  When xml
is requested, it will be processed by using bs4.  For example,

When using the -j option in this manner:

    python3 ./p5.py -j murfreesboro,tn nashville,tn

the program should produce this output:

    58.4 km  between  murfreesboro,tn and nashville,tn

If the -a is used, then the program will visit the given url and
obtain all links (<a> tags) on the page, and only print out the href
values for each link. For example,


"""

import sys
import requests
from bs4 import BeautifulSoup as bs

# When 4 arguments are required in sys
def four_arguments():
    # Note:  origin(city1) = sys.argv[2], destination (city2) = sys.argv[3]
    # url is json url
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins="\
          +sys.argv[2] + "&destinations=" + sys.argv[3]
    # url2 is xml url
    url2 = "https://maps.googleapis.com/maps/api/distancematrix/xml?origins="\
          +sys.argv[2] + "&destinations=" + sys.argv[3]

    # When '-j' is sys.arg[1]
    if sys.argv[1] == '-j':
        req = requests.get(url, headers={}, params={})
        jd = req.json()
        print (" ", jd['rows'][0]['elements'][0]['distance']['text'],\
           "between", sys.argv[2], sys.argv[3])

    # When '-x' is sys.arg[2]
    elif sys.argv[1] == '-x':
        req = requests.get(url2, headers={}, params={})
        soup = bs(req.content, 'html.parser')
        text = soup.text
        text = text.split()
        print (" ", ' '.join(text[-2: ]), "between", sys.argv[2], sys.argv[3])

# When 3 arguments are required in sys 
def three_arguments():
    if sys.argv[1] == '-a':
        req = requests.get(sys.argv[2], headers={}, params={})
        soup = bs(req.content)
        for link in soup.findAll('a'):
            print (" ", link.get('href'))


#  Checks for number of arguments in sys     
if(len(sys.argv) == 3):
    three_arguments()
elif(len(sys.argv) == 4):
    four_arguments()
else:
    print ('error')

