##
##import re
##
##original = 'test loon etta planet aaw meek ziiim try'
##
##print('Original:', original)
##print('Match:', re.findall('[a-z]?[a,e,i,o,u]{2}[a-z]?', original))

import re
import urllib.request, ssl

context = ssl._create_unverified_context()

website = input("Search what page?")

web_page = urllib.request.urlopen(website, context = context)

original = str(web_page.read())

web_page.close()

print("The email addresses in",'\n' + website, '\nare:')

emails = re.findall('[\w.-//+]+[@][\w.-//+]+[.][edu]{3}',original)

for email in emails:
    print(email)
