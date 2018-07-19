#! /usr/bin/env python3
print('Content-type: text/html\n')

import MySQLdb
import cgi

form = cgi.FieldStorage()

string = "i211s18_scottjam"
password = "my+sql=i211s18_scottjam"
db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

html = """
<!doctype html>
<html>
<head><meta charset="utf-8">
<title>Robot Delivery System Confirmation</title></head>
    <body>
    <h1>Robot Delivery System Confirmation</h1>
    <p>You have selected to have a {item} delivered by {method}.</p>
    <p>Your total comes to ${total}</p>
    <h2>Delivery Records</h2>
    <table border="1">
    <tr><th>Item</th><th>Cost</th><th>Method</th><th>Shipping</th></tr>
    {table}
    </table>
    </body>
</html>"""

item = form.getfirst('item', 'unknown item')
cost = form.getfirst('cost', 0)
method = form.getfirst('delivery_method', 'drone')
delivery_fee = 0

if method == 'drone':
  delivery_fee += 10
elif method == 'self driving car':
  delivery_fee += 20
else:
  delivery_fee += 1000

total = cost + delivery_fee
table = ""

try:
  SQL = "INSERT INTO Deliveries (Item, Cost, Method, Shipping)"
  SQL += "VALUES ('{item}', {cost}, '{method}', {delivery_fee});"
  cursor.execute(SQL.format(item=item, cost=cost, method=method, delivery_fee=delivery_fee))
  db_con.commit()
  
  SQL = "SELECT Item, Cost, Method, Shipping FROM Deliveries;"
  cursor.execute(SQL)
  results = cursor.fetchall()

except Exception as e:
  print('<p>Something went wrong with the SQL!</p>')
  print(SQL, "\nError:", e)

else:
  for row in results:
    table += "<tr>"
    for entry in row:
      table += "<td  align='center'>" +str(entry)+ "</td>"
    table += "</tr>"

print(html.format(item = item, method = method, total = total, table = table ))
