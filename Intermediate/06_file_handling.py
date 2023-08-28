### File Handling ###

import xml
import csv
import json
import os

# .txt file

txt_file = open("Intermediate/my_file.txt", "w+") 
txt_file.write("Mi nombre es Ariel \n Mi apellido es Tapia \n 31 años \n Y mi lenguaje preferido es Python ")

#print(txt_file.read())
#print(txt_file.read(10))
#print(txt_file.readline())
#print(txt_file.readline())
#print(txt_file.readlines())
for line in txt_file.readlines():
    print(line)

txt_file.write("Aunque tambien me gusta PHP")
print(txt_file.readline())

txt_file.close()

#os.remove("Intermediate/my_file.txt")

# .json file

json_file = open("Intermediate/my_file.json", "w+")

json_test = {"name": "Ariel",
             "surname": "Tapia",
             "age": 31,
             "languages": ["Python", "PHP", "JavaScript"],
             "website": "artavi.com"}

json.dump(json_test, json_file, indent=4)

for line in json_file.readlines():
    print(line)