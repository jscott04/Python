import re
import urllib.request, ssl
import random
import webbrowser
import os

def wiki_links(url):
    context = ssl._create_unverified_context()
    web_page = urllib.request.urlopen(url, context = context)
    contents = str(web_page.read().decode(errors = 'replace'))
    web_page.close()

    body = re.findall('(?<=<body).+?(?=</body>)', contents, re.DOTALL)[0]
    links = re.findall('(?<=href=").+?(?=")', body)
    wiki_links = [link for link in links if 'wiki' in link and '.org' not in link]
    return wiki_links

##current = input('Where would you like to start?')
##jumps = eval(input("How many jumps?"))
##
##for i in range(jumps):
##    print('Jumping from:', current)
##    pages = wiki_links(current)
##    current = 'http://en.wikipedia.org' + random.choice(pages)
##    print('To:', current, '\n')
##    webbrowser.open_new_tab(current)

def image_list(url):
    context = ssl._create_unverified_context()
    web_page = urllib.request.urlopen(url, context = context)
    contents = str(web_page.read().decode(errors = 'replace'))
    web_page.close()

    pictures = re.findall('(?<=img src=").+?(?=")', contents)
    image_links = [link for link in pictures if 'http' in link]
    return image_links

images = image_list('https://www.sice.indiana.edu/news/index.html')

for pic in images:
    print('Saving', os.path.basename(pic), 'to Pictures/')
    location = os.path.join('Pictures', os.path.basename(pic))
    urllib.request.urlretrieve(pic, location)
