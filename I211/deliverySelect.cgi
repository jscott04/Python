#! /usr/bin/env python3
print('Content-type: text/html\n')
import MySQLdb
import cgi

string = "i211s18_scottjam"
password = "my+sql=i211s18_scottjam"
db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

html = """
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Robot Delivery System</title>
</head>

<body>

<form action="deliveryTable.cgi" method="post">
    <h1>What would you like to have delivered?</h1>
    <table>
    {table}
    </table>
    <h2>Cost: $</h2>
    <input type="text" name="cost" /><br />
    <h2>Delivery Method:</h2>
    <br><input type="radio" name="delivery_method" value="drone">Flying Drone ($10)
    <br><input type="radio" name="delivery_method" value="self driving car">Self Driving Car ($20)
    <br><input type="radio" name="delivery_method" value="giant robot">Giant Robot ($1000)
    <p><button type="submit">Submit</button></p>

</form>
</body>
</html>
"""

table = ''

try:
  SQL = "SELECT * FROM Items;"
  cursor.execute(SQL)
  results = cursor.fetchall()
except Exception as e:
  print('<p>Something went wrong with the SQL!</p>')
  print(SQL, "\nError:", e)
else:
  for row in results:
    table += "<tr>"
    for entry in row:
      table += "<td> <input type='radio' name='item' value='" +str(entry)+ "'>" +str(entry)+ '</td></tr>'

print(html.format(table = table))
