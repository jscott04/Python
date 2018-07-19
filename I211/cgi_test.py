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
        <p>{content}</p>
    </body>
</html>"""

print(html.format(content = 'You have selected to get a ' + form.getfirst('object','unknown item') + 'delivered by' + form.getfirst('delivery_method', 'drone') + '.'))

total = 0
input_cost = eval('cost')
print(input_cost)
