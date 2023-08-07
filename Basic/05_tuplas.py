# tuplas

my_tupla = tuple()
my_other_tuple = (35, 60, 30)

my_tupla = (31, 1.75, "Ariel", "Tapia", "Ariel")
print(my_tupla)
print(type(my_tupla))

print(my_tupla[0])
print(my_tupla[-1])
# print(my_tupla[4]) IndexError
# print(my_tupla[-6]) IndexError

print(my_tupla.count("Ariel")) # cuenta la cant de veces q aparece el valor escrito
print(my_tupla.index("Tapia")) # nos indica el indice del valor escrito
print(my_tupla.index("Ariel"))

my_sum_tuple = my_tupla + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tupla = list(my_tupla) # lo cambie a lista, porque es mutable 
print(type(my_tupla))

my_tupla[4] = "Artavi"
my_tupla.insert(1, "azul")
my_tupla = tuple(my_tupla) # la vuelvo a dejar en tupla, que es inmutable 
print(my_tupla)
print(type(my_tupla))

del my_tupla # eliminar todo, incluso la variable, no solo lo de adentro, el clear borra solo los datos
# print(my_tupla)