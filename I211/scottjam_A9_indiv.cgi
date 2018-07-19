#! /usr/bin/env python3
print('Content-type: text/html\n')

import cgi
form = cgi.FieldStorage()   #parses form data

html = """
<!doctype html>
<html>
<head><meta charset="utf-8">
<title>Robot Delivery System Confirmation</title></head>
    <body>
    <h1>Robot Delivery System Confirmation</h1>
    <p>You have selected to have a {object} delivered by {method}.</p>
    <p>Your total comes to ${total}</p>
    </body>
</html>"""

object = form.getfirst('object','unknown item')
cost = form.getfirst('cost', 0)
method = form.getfirst('delivery_method', 'drone')

total = int(cost)

if method == 'drone':
  total += 10
elsif method == 'self driving car':
  total += 20
else:
  total += 1000

print(html.format(object = object, total = total, method = method))
