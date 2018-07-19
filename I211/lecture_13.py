import re
import urllib.request, ssl

def head_body(url):
    context = ssl._create_unverified_context()
    web_page = urllib.request.urlopen(url, context = context)
    contents = str(web_page.read().decode(errors = 'replace'))
    web_page.close()
    head = re.findall('(?<=<head).+?(?=</head>)', contents, re.DOTALL)[0]
    body = re.findall('(?<=body).+?(?=</body>)', contents, re.DOTALL)[0]
    return head, body

website = input('Searching:')
head, body = head_body(website)
print('Head:', head)
print('Body:', body)

def wiki_links(url):
    context = ssl._create_unverified_context()
    web_page = urllib.request.urlopen(url, context = context)
    contents = str(web_page.read().decode(errors = 'replace'))
    web_page.close()

    body = re.findall('(?<=<body).+?(?=</body>)', contents, re.DOTALL)[0]
    links = re.findall('(?<=href=").+?(?=")', body)
    wiki_links = [link for link in links if 'wiki' in link and '.org' not in link]
    return wiki_links

url_list = wiki_links('http://en.wikipedia.org/wiki/Airy_wave_theory')

for url in url_list:
    print('\t', url)
