# Jared Scott
# Lab Group 5

import random

# Problem 1

def getGuess():
    guess = input("Enter a 4 letter guess:")
    guess.isalpha() #user enters a guess, .isalpha() makes sure its all letters

    while True:
        if guess.isalpha() and len(guess) == 4:
            return guess #returns guess if it is 4 letters long
        else:
            guess = input("Guess is invalid, Enter a four letter guess: ")
            # must enter another guess if not

score = 0
word = 'cart' #correct word
word_lst = [] #empty list
    
for i in range(len(word)):
    word_lst.append(word[i]) #for loop appends each letter to the empty list

while score < 4:
    guess = getGuess()
    guess_lst = []
    
    for i in range(len(guess)):
        guess_lst.append(guess[i]) #appends each letter to the guess list

    for i in range(len(word_lst)):
        if guess_lst[i] == word_lst[i]: # for every position, if the letters are equal it will add 1 to the score
            score += 1
    print('Your score:', score)

    if score != 4: #resets the score to 0 if all 4 letters were not guessed correctly
        score = 0
        
# Problem 2

options = ['rock', 'paper', 'scissors'] # possible options

user = input('Choose rock, paper, or scissors:')
comp = random.choice(options) # chooses an option at random from options list

print(comp)
if user.lower() not in options: #If the user inputs something other than rock paper or scissors, gives them a message saying so
    print('That was not a valid option.')

if user.lower() == comp: #if user input and computer choice are the same, it is a tie
    print('Tie.')

if user.lower() == 'rock':
    if comp == 'scissors':
        print('You win!')
    else:
        print('You lost.')
    
if user.lower() == 'scissors':
    if comp == 'rock':
        print('You lost.')
    else:
        print('You won!')
    
if user.lower() == 'paper':
    if comp == 'rock':
        print('You won!')
    else:
        print('You lost.')

# compares the two choices and determines the winner
