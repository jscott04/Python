import xml.etree.ElementTree as ET

root = ET.parse(source = 'students.xml')


elements = root.iter()

##for elem in elements:
##    print('Tag Name:', elem.tag)
##    print('Tag Text:', elem.text)
##    print('Children:', list(elem))
##    print('-' * 20)


students = root.iter('Student')

##print('The students are:')
##for student in students:
##    print(student.find('name/first').text, student.find('name/last').text)


total_fees = 0

fees = root.findall('Student/fees')

for fee in fees:
    total_fees += int(fee.text)
    
print('The total amount of student fees is:', '$' + str(total_fees))

