##headers = ['Name', 'Age', 'Hometown']
##
##
##data = []
##
##while len(data) < 5:
##    name = input('Please enter a name: ')
##    age = input('Please enter an age: ')
##    hometown = input('Please enter a hometown: ')
##    lst = [int(age), name, hometown]
##    data.append(lst)
##
##sorted_lst = sorted(data)
##
##string_template = "{}\t{}\t{}"
##
##print(string_template.format(headers[0], headers[1], headers[2]))
##
##print('-' * 15)
##for item in sorted_lst:
##    print(string_template.format((item[1], item[0], item[2])))


lst = [6,3,2,5,7,1,1,2]
sorted_lst = []
while lst:
    min_value = min(lst)
    sorted_lst.append(min_value)
    lst.remove(min_value)

print(sorted_lst)
