# strings

my_string = "Mi string"
my_other_string = 'Mi otro string'

print(len(my_string))
print(len(my_other_string))


print(my_string + " " + my_other_string)

my_new_line_string = "\tEste es un string \ncon salto de linea"

print(my_new_line_string)

nombre, apellido, edad = "Ariel", "Tapia", 31

print("Mi nombre es {} {} y mi edad es {}".format(nombre, apellido, edad))
print("Mi nombre es %s %s y mi edad es %d" %(nombre, apellido, edad))
print("Mi nombre es "+ nombre +" "+ apellido + " y mi edad es "+ str(edad)) # no es optimo
# print(f"Mi nombre es {nombre} {apellido} y mi edad es {edad}") # no funca
print(f"Mi nombre es {nombre} {apellido} y mi edad es {edad}")


# desempaquetado de caracteres 
languaje = "python"
a, b, c, d, e, f = languaje
print(a)
print(b)

# Division 

languaje_slice = languaje[1:3]
print(languaje_slice)

languaje_slice = languaje[1:]
print(languaje_slice)

languaje_slice = languaje[-1]
print(languaje_slice)

languaje_slice = languaje[0:6:2]
print(languaje_slice)

# Reversa

reserved_languaje = languaje[::-1]
print(reserved_languaje)

# Funciones 

print(languaje.capitalize())
print(languaje.upper())
print(languaje.count("t"))
print(languaje.isnumeric())
print("1".isnumeric())
print(languaje.lower())
print(languaje.upper().isupper())
print(languaje.lower().isupper())
print(languaje.startswith("py"))
