##num_sum = 0
##user_in = ""
##
##while user_in.upper() != "STOP":
##    user_in = input("Please enter a number or STOP:")
##
##    if user_in.upper() != "STOP": 
##        num_sum += int(user_in)
##    else:
##        print("The total sum is", num_sum)
##
##count = 0
##evens = []
##odds = []
##others = []
##
##while count != 10:
##    num = input("Please enter a number: ")
##    count += 1
##    
##    if float(num) % 2 == 0:
##        evens.append(int(num))
##    elif float(num) % 2 == 1:
##        odds.append(int(num))
##    else:
##        others.append(float(num))
##        
##print('The results are:')
##print('Evens: ', evens)
##print('Odds: ', odds)
##print('Others: ', others)

scores = {'Dave': 125, 'Abby': 100, 'Carrie': 275, 'Ben': 150}
names = []

for item in scores.keys():
    names.append(item)
    
print("Current Players:")
print(sorted(names))

user_input = input("Please enter a Player Name:")
if user_input in scores.keys():
    print("The score for", user_input, "is", scores.get(user_input), '.')
else:
    print("The score for", user_input, "is not found.")



