import re
import urllib.request, ssl

def pageload(url):
    context = ssl._create_unverified_context()
    web_page = urllib.request.urlopen(url, context = context)
    contents = str(web_page.read().decode(errors = 'replace'))
    web_page.close()
    return contents

page = pageload('https://en.wikipedia.org/wiki/2017_in_film')


table = re.findall('(?<=of 2017</caption>).+?(?=</table>)', page, re.DOTALL)[0]
highest_grossing = re.findall('(?<=<i><a href=").+?(?=")', table)

print("Wiki links for top 10 grossing films in 2017:")
print('-'*30)

for movie in highest_grossing:
    print(movie)

print('-'*30)

movie = input("Please select a top 10 movie:")

for link in highest_grossing:
    if movie in link:
        source = pageload('https://en.wikipedia.org'+link)

        plot = re.findall('(?<=id="Plot">Plot</span>).+?(?=<span class="mw-headline")', source, re.DOTALL)
        # first parenthesis: starts at id='Plot' in the html file
        # .+? : includes the paragraphs after Plot</span>
        # second parenthesis: ends at the <span class='mw-headline" of the next sections header
        print(plot[0])





