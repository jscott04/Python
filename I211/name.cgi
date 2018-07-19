#! /usr/bin/env python3
print('Content-type: text/html\n')

import cgi

form = cgi.FieldStorage()   #parses form data

html = """
<!doctype html>
<html>
<head><meta charset="utf-8">
<title>Form in CGI</title></head>
    <body>
        <h1>Greetings!</h1>
        <p>{content}</p>
    </body>
</html>"""

print(html.format(content = 'Hello,' + form.getfirst('username','Who are you?')))
