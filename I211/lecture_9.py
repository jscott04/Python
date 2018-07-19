import csv

data = open("companies.csv", "r")

companies = list(csv.reader(data))


company_dict = {}

state = input("Search for companies in what state?")

for line in companies:
    if line[6].upper() == state.upper():
        company_dict[line[2]] = line[11]

print('-' * 70)

for item in company_dict:
    print(item + (' ' * (30 - len(item))), company_dict[item])

    
    
    


