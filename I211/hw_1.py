#Problem 2

# Import Random Module
# User selects rock, paper, or scissors
# Computer randomly selects rock, paper, or scissors

#Check if the users selection and the computers are the same
#   If so, print a message that signifies a tie

#If the user selected rock and the computer selected scissors
#   print a message that says the user won
#If the user selected rock and the computer selected paper
#   print a message that says the user lost

#If the user selected paper and the computer selected rock
#   print a message that says the user won
#If the user selected paper and the computer selected scissors
#   print a message that says the user lost

#If the user selected scissors and the computer selected paper
#   print a message that says the user won
#If the user selected scissors nad the computer selected rock
#   print a message that says the user lost

#Problem 3

string = input('Please enter a string: ') #string inputted by user
str_lst = list(string) #creates a list out of the string
str_lst.reverse() #reverses the order of the list

new_str = ''  #empty string defined as new_str

for item in str_lst:
    new_str += item     #for every item in the str_lst, it is added to the new string

print(new_str) #prints the new, reversed string


#Problem 4

lst1 = [3, 2, 1, 0]
lst2 = [5, 6, 8, 9] #test lists

def match(lst, lst1): #defined a function match() with 2 arguments, lst and lst1
    value = False     #first set value to False, the default value
    
    for item in lst:        #for loop that loops through the items in the first lst
        if item in lst1:    #If the item is in the second list, it will update value to True
            value = True
    return value
    #After the loop has ended, value is returned


