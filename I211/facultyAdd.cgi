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
<html>
    <head><title>Faculty Table</title></head>
    <body>
      <h1>New Faculty Member Added!</h1>
      <table border='1' width='100%'>
      <tr><th>FacultyID</th><th>Name</th><th>Title</th><th>Email</th><th>Areas</th><th> </th></tr>
      {content}
      </table>
     </body>
</html>"""

name = form.getfirst('name')
title = form.getfirst('title')
email = form.getfirst('email')
areas = form.getfirst('areas')

try:
  SQL = "INSERT INTO Faculty (Name, Title, Email, Areas)"
  SQL += "VALUES ('{name}', '{title}', '{email}', '{areas}');"
  cursor.execute(SQL.format(name=name, title=title, email=email, areas=areas))
  db_con.commit()

  SQL = "SELECT * FROM Faculty;"
  cursor.execute(SQL)
  results = cursor.fetchall()

except Exception as e:
  print('<p>Something went wrong with the SQL!</p>')
  print(SQL, "\nError:", e)

else:
  table = ""
  for row in results:
    table += "<tr>"
    for entry in row:
      table += "<td  align='center'>" +str(entry)+ "</td>"
    table += "<td align='center'><a href='facultyDelete.cgi?fid='" + str(row[0]) + ">Delete</a></td></tr>"

print(html.format(content = table))
