import re
import urllib.request, ssl

# Lab Problem 1

files = open('quote.txt','r')
quotes = files.read()
files.close()

cap_words = re.findall('[A-Z]{1}[a-z]*', quotes)
print('Words beginning with a capital letter:', cap_words)

ing_words = re.findall('[A-Za-z]*ing', quotes)
print("Words ending in 'ing':", ing_words)

aa_words = re.findall('[A-Za-z]*[a]{1}[b-z]*[a]{1}[b-z]*', quotes)
print("Words with two a's in them:", aa_words)

# Lab Problem 2

context = ssl._create_unverified_context()
website = 'http://www.soic.indiana.edu/about/contact/index.html'
web_page = urllib.request.urlopen(website, context = context)

original = str(web_page.read())
web_page.close()

phone_numbers = re.findall('\([0-9]{3}\)[ ]{1}[0-9]{3}[\-]{1}[0-9]{4}', original)

print('Searching:', website)
print('Found the following phone numbers:')
for num in phone_numbers:
    print(num)
