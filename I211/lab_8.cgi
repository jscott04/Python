#!/usr/bin/env python3

import cgitb
cgitb.enable()

afi_rank = []

file1 = open('top100moviesAFI.txt', 'r')
afi = file1.read()
file1.close()

afi_contents = afi.split('\n')

afi_count = 1
for item in afi_contents:
    afi_rank.append([item, afi_count])
    afi_count += 1

rt_rank = []

file2 = open('top100moviesRT.txt', 'r')
rt = file2.read()
file2.close()

rt_contents = rt.split('\n')
rt_count = 1

for item in rt_contents:
    rt_rank.append([item, rt_count])
    rt_count += 1
print(rt_rank)

html = """<!doctype html>
<html>
<head>
    <meta charset = "utf-8">
    <title>Table CIGI/title>
</head>
<body>
    <table border = 1> (content)</table>
</body>
</html>"""

table = ""

for item in rt_contents:
	table += '<tr> 
	for j in item:
		table += '<td>' + i + '</td>'
	table += '</tr>'
out.write(html.format(content = table))
out.close()
print(table)
