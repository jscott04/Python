import xml.etree.ElementTree as ET #imports ElementTree

root = ET.parse('library.xml') #parses through library.xml
books = root.iter('book') # looks through objects with book tag

# Problem 1


def display_book(bookID): # defines function display_book with bookID as sole parameter
    for item in books:  # loops through each item in books
        if bookID == item.attrib['id']: # compares book id attribute to parameter given by user
            print(item.find('author').text) # finds author tag and prints the text
            print(item.find('title').text) # find title tag and prints the text
            print(item.find('genre').text) # finds genre tag and prints the text
            print(item.find('price').text) # finds price tag and prints the text

# Problem 2

for item in books: # loops through each item in books
    release = item.find('publish_date').text.split('-')
    # finds the publish_date tag, splits the text at the '-', assigns it to variable release
    genre = item.find('genre').text # finds the genre tag and assigns it to variable genre
    if release[1] == '12' and genre == 'Computer': # release[1] is the month, if the month is 12 and genre is Computer
        print(item.find('title').text)
        print(item.find('author').text)
        print(item.find('price').text, '\n')
        # each line finds the given tag and prints the text, a newline is printed after price
        

# Problem 3

genres = root.findall('book/genre') #finds all sub-elements in the path book/genre, (all genres)

for item in genres: # loops through each genre tag
    print(item.text) # prints the text


