
afi_rank = {}
rt_rank = {}

file1 = open('top100moviesAFI.txt', 'r')
afi = file1.read()
file1.close()

afi_contents = afi.split('\n')
afi_count = 1

for item in afi_contents:
    afi_rank[item] = afi_count
    afi_count += 1

file2 = open('top100moviesRT.txt', 'r')
rt = file2.read()
file2.close()

rt_contents = rt.split('\n')
rt_count = 1

for item in rt_contents:
    rt_rank[item] = rt_count
    rt_count += 1

movies = []

for key in afi_rank.keys():
     movies.append(key)
for key in rt_rank.keys():
    if key not in movies:
        movies.append(key)

movies_rank = [['Movie', 'AFI Rank', 'RT Rank']]

for item in sorted(movies):
    if item in afi_rank.keys():
        if item not in rt_rank.keys():
            movies_rank.append([item, afi_rank[item], '--'])
        else:
            movies_rank.append([item, afi_rank[item], rt_rank[item]])
    else:
        movies_rank.append([item, '--', rt_rank[item]])


out = open('movie_table', 'w')

html = """<!doctype html>
<html>
<head>
	<meta charset="utf-8">
	<title>Top 100 Movie Comparisons</title>
</head>
<body>
    <table border = 1>{content}</table>
</body>
</html>"""

table = ""

for lst in movies_rank:
    table += '<tr>'
    for item in lst:
        table += '<td>' + str(item) + '</td>'
    table += '</tr>'

out.write(html.format(content = table))
out.close()

print('Finished Writing.')

    


    


