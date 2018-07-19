import xml.etree.ElementTree as ET

root = ET.parse(source = 'students.xml')

elements = root.iter()

for elem in elements:
    if elem.attrib:

        print('Attributes', elem.attrib)
        print('-' * 20)

fee = root.find('Student/fees')
print('Units:', fee.attrib['units'])
print('Country:', fee.attrib['c'])
