#!/usr/bin/env python3

import cgitb
cgitb.enable()

html = """<!doctype html><html><head><meta charset = "utf-8"><title>Table CIGI/title></head>
<body><table border = 1> (content)</table></body></html>"""

table = ""

i = 0
for i in range(10):
	table += '<tr> 
	for j in range(10):
		table += '<td> Column' + str(i) + '</td>'
	
out.write(html.format(content = table))
out.close()
print(table)