# Problem 1

# hexcolor = re.findall([A-Fa-f0-9]{6}], website)

# Problem 2

# 1. Import modules
# 2. Assign the given website to a variable
# 3. Open the website
# 4. .read the website and assign it to a variable
# 5. Use .findall to create a pattern to find the wins
# 6. Use .findall to create a pattern to find the losses
# 7. Set the variable difference equal to 0
# 8. Create a for loop to loop through the wins list,
#    get the scores, and add the difference to the variable difference
# 9. Repeat step 8 for the losses list
# 10. Use length of wins list and length of losses to get the number of wins/losses
# 11. Print statements for wins, losses and difference

# Problem 3

import re
import urllib.request, ssl

context = ssl._create_unverified_context()

website = 'http://cgi.soic.indiana.edu/~dpierz/mbball.html' # set the variable website to the given website

web_page = urllib.request.urlopen(website, context = context) # opens the website
original = str(web_page.read()) #reads the website and sets original to the string of the website
web_page.close() # closes the open web_page

wins = re.findall('[W]{1}[ ]{1}[0-9]{2}[-][0-9]{2}', original) #finds every win along with the score
loss = re.findall('[L]{1}[ ]{1}[0-9]{2}[-][0-9]{2}', original) #finds every loss along with the score

difference = 0 # set the variable difference equal to 0

for item in wins:
    score1 = int(item[2:4]) # sets score1 equal to the first score
    score2 = int(item[5:]) # sets score2 equal to the second teams score
    difference += abs(score1-score2) # adds the absolute value of score1 - score2 to the difference
    
for item in loss: # loops through each item in the loss list
    score1 = int(item[2:4]) #sets score1 equal to the first score
    score2 = int(item[5:]) # sets score2 equal to the second score
    difference += abs(score1-score2) # adds the absolute value of score1 - score2 to the difference
    
print('Wins:', len(wins)) # prints the number of wins
print('Losses:', len(loss)) # prints the number of losses
print('Total Difference:', difference) # prints the total difference
