#! /usr/bin/env python3
print('Content-type: text/html\n')
import MySQLdb

string = "i211s18_scottjam"
password = "my+sql=i211s18_scottjam"

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

print('Connection Successful!')
