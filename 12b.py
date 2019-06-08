#
#Scraping Numbers from HTML using BeautifulSoup.
#In this assignment you will write a Python program similar to
#http://www.py4e.com/code3/urllink2.py.
#The program will use urllib to read the HTML from the data files below,
# and parse the data, extracting numbers
#and compute the sum of the numbers in the file.
#We provide two files for this assignment.
#One is a sample file where we give you the sum for your testing
#and the other is the actual data you need to process for the assignment.
#Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_242087.html (Sum ends with 58)

#print('Starting')
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

count = 0
num = 0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_242087.html"
#print(url)
html = urlopen(url, context=ctx).read()
#print(html)
soup = BeautifulSoup(html, "html.parser")


# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
   # Look at the parts of a tag
   #print('TAG:',tag)
   #print(URL:',tag.get('span', None))
   num = num + float(tag.contents[0])
   count = count + 1
print('Count:', count)
print('sum', num)
