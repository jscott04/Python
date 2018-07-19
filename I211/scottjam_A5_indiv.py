# Problem 1

# The %A placeholder is used to get full name of the day of the week, the full name is displayed as a title.

# Problem 2

# 1.) import csv and datetime module
# 2.) open the shoprecords.csv file and save in a variable
# 3.) create a list/tuple that has the weekend days
# 4.) read the file using .DictReader() method
# 5.) loop through each item in the file
# 6.) use the .split() method to split the date given as a string, then format the date using integers
# 7.) use the formatted date along with the .strftime() method to get the day of the week
# 8.) determine if the day the item was purchased is in the weekend days list/tuple
# 9.) print the item name if it occured on a weekend, do nothing if it wasnt

# Problem 3

import csv #imports csv module
import datetime #imports datetime module

data = open('ShopRecords.csv', 'r') #opens the file 'ShopRecords.csv'

records = csv.DictReader(data) #reads the file as a dictionary in the records variable
weekend = ('Saturday', 'Sunday') #tuple that has the weekend days

for item in records: #for loop that loops through each item in records
    date = item['Date'].split('/') #splits the date string by the forward slash and creates a list
    format_date = datetime.date(int(date[2]), int(date[0]), int(date[1])) #formats the date, used for .strftime() method
    weekday = format_date.strftime("%A") #uses the .strftime() method with %A placeholder to get the day of the week the item was purchased

    if weekday in weekend:
        print(item['Item']) #if the day of the week the item was purchased is in the weekend tuple, the item name is printed

    

