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

json_file.close()

with open("Intermediate/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("Intermediate/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

# csv file

csv_file = open("Intermediate/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Ariel", "Tapia", 31, "Python", "Artavi.com"])
csv_writer.writerow(["Brais", "Moure", 35, "Python", "https://moure.dev"])

csv_file.close()

with open("Intermediate/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)
        
# xlsx file

# xml file