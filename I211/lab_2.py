
def getGuess():
    guess = input("Enter a 4 letter guess:")
    guess.isalpha()

    while True:
        if guess.isalpha() and len(guess) == 4:
            return guess
        else:
            guess = input("Guess is invalid, Enter a four letter guess: ")
    

score = 0
word = 'cart'
word_lst = []
    
for i in range(len(word)):
    word_lst.append(word[i])

while score < 4:
    guess = getGuess()
    guess_lst = []
    
    for i in range(len(guess)):
        guess_lst.append(guess[i])

    for i in range(len(word_lst)):
        if guess_lst[i] == word_lst[i]:
            score += 1
    print('Your score:', score)

    if score != 4:
        score = 0
        
    



##data = ['50 apples\n', '25 pears\n', '10 oranges\n']
##groceries = {}
##
##for item in data:
##    num, name = item.strip().split(' ')
##    groceries[name] = int(num)
##
##print(groceries)
##
##import random
##
##def playGame():
##    play = True
##    
##    while play:
##        print("Welcome to Fortnite")
##        loc = ['MM', 'TT', 'SS']
##        wep = ['pistol', 'shotgun', 'ar']
##        
##        weapons = input("Choose your weapon: (pistol, shotgun, AR) ")
##
##        valid_wep = True
##        valid_loc = True
##        
##        if weapons.lower() not in wep:
##            valid_wep = False
##        
##        
##        location = input("Choose where you land: (MM, TT, SS)")
##
##        if location.upper() not in loc:
##            valid_loc = False
##            
##
##        place = random.randrange(1,100)
##
##        if not valid_wep:
##            print("You didn't choose a valid weapon, you lose.")
##        elif not valid_loc:
##            print("You didn't choose a valid location, you lose.")
##        elif place < 1:
##            print('Congrats! You finished first!')
##        elif place < 25:
##            print('You finished in the top 25!')
##        else:
##            print("Sorry, you didn't finish in the top 25")
##
##        play_again = input("Do you want to play again?")
##
##        if play_again.lower() == 'no':
##            play = False
##        
##playGame()        



        
