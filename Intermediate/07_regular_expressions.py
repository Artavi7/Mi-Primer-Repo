### Regular Expressions ###

import re

# match

my_string = "Esta es la leccion 7: Leccion llamada Expresiones Regulares"
my_other_string = "Esta no es la leccion 6: Manejo de Ficheros"

match = re.match("Esta es la leccion", my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])

match2 = re.match("Esta no es la leccion", my_other_string, re.I)
# if not(match == None): #esta es otra forma
if match2 != None:
    print(match2)
    start, end = match2.span()
    print(my_other_string[start:end])

#print(re.match("Expresiones Regulares", my_string))

# search

search = re.search("leccion", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

# findall

findall = re.findall("leccion", my_string, re.I)
print(findall)

# split

print(re.split(":", my_string))

# sub

print(re.sub("[l|L]eccion", "LECCIÓN", my_string))
print(re.sub("Expresiones Regulares", "RegEx", my_string))

### Regular Expressions Patterns ###

pattern = r"[lL]eccion"
print(re.findall(pattern, my_string))

pattern = r"[lL]ección|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"\d"
print(re.findall(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l].*"
print(re.findall(pattern, my_string))

email = "atapia@gorecoquimbo.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "atapia@gorecoquimbo.com.mx"
print(re.findall(pattern, email))