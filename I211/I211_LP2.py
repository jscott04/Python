# Jared Scott, scottjam
# Lab Practical 2

import re, urllib.request, ssl #import modules

context = ssl._create_unverified_context() 

website = 'http://cgi.soic.indiana.edu/~dpierz/news.html' # assign the given website to variable website
web_page = urllib.request.urlopen(website, context = context) # urlopen() the website and assign it to the variable web_page
contents = str(web_page.read().decode(errors = 'replace')) # read the web_page, set it to a string, and assign it to contents
web_page.close() # close web_page

headlines = re.findall('(?<=span itemprop="headline">).+?(?=</span>)', contents)
# finds the headlines of the news articles, news article headlines are between the <span></span> with itemprop='headlines'

print('Searching:', website) # prints searching and the url

##for item in headlines:
##    print(item, '\n')   # prints each headline on a new line for section 2
                          # commented out to do section 3

word = input('Please enter a word to search for:') #takes an input from the user

for item in headlines: # loops through each headline
    if word.lower() in item.lower(): # if the user input is in the headline, case-insensitive
        print('\t',item, '\n')      # prints the headline (\t, \n were for formatting purposes, easier to read in shell)
        


