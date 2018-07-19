import csv
import datetime

def listCharacters():
    data = open("star-wars.csv", "r")

    characters = csv.DictReader(data)

    print('-' * 80)
    print("MAIN CHARACTERS\nStar Wars: Episode VII: The Force Awakens (2015)")
    print('-' * 80)

    for item in characters:
        print(item['character'], ' ' * (30 - len(item['character'])), item['name'], ' ' * (30 - len(item['name'])), item['birthday'])




def getBios():
    data = open("star-wars.csv", "r")

    characters = csv.DictReader(data)
        
    print('-' * 80)
    print("BIOS")
    print('-' * 80)

    oldest = 0
    oldest_char = ''
    
    youngest = 100
    youngest_char = ''

    friday_cast = []
    
    for item in characters:
        birth = item['birthday'].split('/')
        
        now = datetime.date.today()
        bday = datetime.date(int(birth[2]), int(birth[0]), int(birth[1]))
        dob = bday.strftime("%A, %B %d, %Y.\n")
        age = now - bday

        years = int(age.days/365)

        if years > oldest:
            oldest = years
            oldest_char = item['name']
        elif years < youngest:
            youngest = years
            youngest_char = item['name']

        if 'Friday' in dob:
            friday_cast.append(item['name'])
        print(item['character'], 'is played by', item['name'] + ',\nwho was born on', dob + item['name'], 'is', years, 'years old.\n')

    print("The oldest cast member is", oldest_char, 'who is', oldest, 'years old.')
    print('The youngest cast member is', youngest_char, 'who is', youngest, 'years old.')
    
    print("\nCast members born on a Friday:")
    for item in friday_cast:
        print(item)

        
getBios()
