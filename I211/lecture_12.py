import re
import urllib.request, ssl

##file = open('message.txt','r')
##message = file.read()
##file.close()
##
##redact = re.sub('[A-Z]{1}[\w]+[ ]{1}[A-Z][\w]+|[\w]+[@]{1}[\w]+[.][\w]+|\([0-9]{3}\)[ ]{1}[0-9]{3}[\-]{1}[0-9]{4}', 'redacted', message)
##
##print('Reading in from: message.txt')
##print('Redacted file saved as: messageRedacted.txt')
##
##file_out = open('messageRedacted.txt', 'w')
##file_out.write(redact)
##file_out.close()

context = ssl._create_unverified_context()
website = "http://www.sice.indiana.edu/about/contact/index.html"
web_page = urllib.request.urlopen(website, context = context)

original = str(web_page.read())
web_page.close()

links = re.findall("[https://]{8}[\w./]+", original)

print('Searching:', website)
print('Found the following links:')
for link in links:
    print(link)
