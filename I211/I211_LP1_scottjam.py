
# Functions

def show_list(lst): #defining show_lst function
    #if the list has a length of one, the password is found and prints a message saying so, if not then it displays a different message
    if len(lst) > 1:
        print("The current possible passwords are:\n" + "-" * 30)
    else:
        print("Password Found!\n" + '-' * 30)
    print_lst = [print(item) for item in lst] # could not figure out how to get 5 words on one line, for loop prints each item on a separate line
    print('(' + str(len(lst)), 'possible)\n') # number of possible passwords


#Strings and Variables
    
vowels = ['a', 'e', 'i', 'o', 'u'] # vowel list used for clues
let = 'abcdefghijklnopqrstuvwxyz' # created a string variable called let that has each letter in the alphabet. used for bonus
double_let = [char * 2 for char in let] # i used list comprehension to create a list called double_let. for each character in the string let,
                                        #the character repeated twice is added to double_let. used for bonus


# Original Password List
file =[line.strip() for line in open("passwords.txt", "r")] #importing passwords.txt into a list called file
show_list(file) #runs show_list function on the original list file


# Clue 1

clue1 = [word for word in file if len(word) >= 6] #adds the word to the list clue1 if the length of the word is greater than or equal to 6

# Clue 2

clue2 = [word for word in clue1 if([char for char in word if char.isalpha()])]
# loops through the list clue1. adds the word to the list clue2 if at least one character is a letter.
# the if statement loops through each character in the word and checks if its in the alphabet using the .isalpha() method

# Clue 3

clue3 = [word for word in clue2 if word[0].lower() not in vowels and word[1].lower() in vowels]
# if words[0] (first letter) is not in the vowels list and word[1] (second letter) is in the vowels list, the word is added to the list clue3.
# I used the .lower() method on word[0] and word[1] so i did not have to type capital vowels in the vowel list

# Clue 4

clue4 = [word for word in clue3 if len([char for char in word if char not in vowels]) >= 2 * len([char for char in word if char in vowels])]
# The if statement has two list comprehensions. the first adds the character to the list if it is not in vowels, and the second adds the character to the list if it is for each word in clue3.
# The if statement then compares the lengths of each list and if the first list is greater than or equal to 2 times the second list, then the word is added to the list clue4

# Bonus

bonus = [word for word in clue4 if[char for char in double_let if char in word]]
# The if statement loops through each item in the list double_let and if the item is in the word,
# the word is added to the list bonus. This is repeated for each word in clue4



# Clues and show_list functions
#The code below prints each clue, and runs the show_list function on each clue       
print('Clue 1: The password is at least 6 characters long.\n') 
show_list(clue1) 
print('Clue 2: The password contains at least 1 letter.\n') 
show_list(clue2)
print('Clue 3: The password does not start with a vowel, but the second character is a vowel.\n') 
show_list(clue3)
print('Clue 4: The password has at least twice as many consonants as vowels.\n') 
show_list(clue4)
print('Bonus: The password has the same letter twice in a row.\n')
show_list(bonus)
