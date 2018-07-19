# Problem 1: Python Standard Documentation

# The Standard Documentation for Python is found under Help in the IDLE toolbar.
# If the user opens the Help dropdown list and selects Python docs,
# a webpage with the documentation will be opened. The user can also simply press F1.

# Problem 2: Algorithm for Problem 3

# 1. Import modules
# 2. Get a path from the user
# 3. Join the path from the user with the current directory
# 4. Set the joined path as the default
# 5. Create a list of all items in the directory 
# 6. Loop through the items in the lists
# 7. If the item is a file and has draft in the file name, replace it with final
# 8. Append a string that says Edited on with todays date to the end of the file

# Problem 3: Renaming files

import os           #imported the os module
import datetime     #imported the datetime module

file_path =input("Please enter a directory path:")  #user inputs a directory path

path = os.path.join(os.getcwd(), file_path)
os.chdir(path)
#os.path.join() creates a directory path with the given arguments.
#I used the os.getcwd() to get the current directory and joined it with file_path (path given by user)
#os.chdir(path) changes the directory Python 'sees' to the one defined in path

filenames = os.listdir(os.getcwd()) #sets filenames to the list of files in the current directory

for file in filenames: #for loop that loops through filenames, each item is defined as file
    if os.path.isfile(file): #checks if file is a file
        if 'draft' in file: #if the string 'draft' is in the file name
            now = datetime.date.today() #set now equal to todays date

            edit_file = open(file, 'a') #opens file in append mode
            edit_file.write('Edited on ' + str(now)) #writes Edited on and todays date to the end of the file    
            edit_file.close() #closes file
                
            os.rename(file, file.replace('draft', 'final'))
            #os.rename gives the file a new name, file.replace replaces the string 'draft' with 'final' in the

               
        
            
            



