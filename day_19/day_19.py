###FILE HANDLING###
# File handling is an import part of programming which allows us to create, read, update and delete files. In Python to handle data we use open() built-in function. We can also handling different file formats(.txt, .json, .xml, .csv, .tsv, .excel)

# File with txt Extension
# open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update 
# "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# Opening Files or Reading
#read(): read the whole text as string
f = open('./reading_file_example.txt')
print(f)
text = f.read()
f.close()

#readline(): read the text line by line
f = open('./reading_file_example.txt')
print(text)
line = f.readline()
print(line)
f.close()

#readlines(): read the text line by line and return a list of lines
f = open('./reading_file_example.txt')
lines = f.readlines() 
print(lines)
f.close()

#splitlines(): read the text line by line and return a list of lines
f = open('./reading_file_example.txt')
lines = f.read().splitlines() 
print(lines)
f.close()

# Opening Files for Writing and Updating
# we must add a mode as parameter to the open() function:
# "a" - append - will append to the end of the file, if the file does not it creates a new file.
with open('./reading_file_example.txt','a') as f:
   f.write('This text has to be appended at the end')
# "w" - write - will overwrite any existing content, if the file does not exist it creates.
with open('./reading_file_example.txt','w') as f:
   f.write('This text will be written in a newly created file')

# Deleting Files
import os
if os.path.exists('./example.txt'):
    os.remove('./example.txt')
else:
    print('The file does not exist')

# File Types
# File with json Extension
# JSON stands for JavaScript Object Notation. Actually, it is a stringified JavaScript object or Python dictionary.
    
#Changing JSON to Dictionary
import json
# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])

#Changing Dictionary to JSON
import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# let's convert it to  json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(type(person_json))
print(person_json)

#Saving as JSON File
import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('./json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)

# File with csv Extension
import csv
with open('./bio.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a programmer. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')

# File with xlsx Extension "You should do all in start.sh for run this code"
import xlrd
excel_book = xlrd.open_workbook('./Bio.xls')
print(excel_book.nsheets)
print(excel_book.sheet_names)

# File with xml Extension
import xml.etree.ElementTree as ET
tree = ET.parse('./example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)


###EXERCISE###
##Lvl 1
    