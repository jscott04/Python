##file_name = input('Please enter a file name: ')
##
##lines = [line.strip() for line in open(file_name, "r")]
##all_words = [word.split(' ') for word in lines]
##words = [word for line in lines for word in line.split()]
##two_v_words = [word for word in words \
##               if len([let for let in word if let in 'aeiou']) >= 2]
##
##print('All words in the file:', lines)
##print('The words in the file that contain 2 or more vowels:', two_v_words)

translate = {'1':'i', '3':'e','4':'a','5':'s','7':'t'}

phrase = input('Please enter a phrase:')

words = [translate[let] if let in translate.keys() else let for word in phrase for let in word]

print('Output:', ''.join(words))
