##def valid_pass():
##    while True:
##        password = input("Please enter a password:")
##        if len(password) > 8:
##            return password
##            break
##        else:
##            print("That was not a valid password, please try again.")
##
##my_pass = valid_pass()
##
##print('Your valid password is: ', my_pass)

lst = [1, 1, 1, 2, 2, 2, 2, 2, 4, 3, 3, 3, 3, 3, 3]

def count(lst):
    dict1 = {}
    
    print("The list is: ", lst)
    
    for i in range(len(lst)):
        if lst[i] in dict1:
            dict1[lst[i]] += 1
        else:
            dict1[lst[i]] = 1
    return dict1

count = count(lst)
print('Number', 'Count', sep = '\t')
for item in dict1.items():
    print(item[0], item[1], sep = '\t')
