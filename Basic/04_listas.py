# Listas 

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Ariel", "Tapia"]

print(my_list)
print(len(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(30)) # retorna el numero de veces de cierto valor, en este caso 30
#print(my_other_list[4]) IndexError
#print(my_other_list[-5]) IndexError

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

print(my_list + my_other_list)
# print(my_list - my_other_list) error

my_other_list.append("GORE") # agrega al final
print(my_other_list)

my_other_list.insert(1, "Rojo") # 
print(my_other_list)

my_other_list[1] = "Azul"

my_other_list.remove("Azul")
print(my_other_list)

my_list.remove(30) # elimina el primer valor 30 encontrado
print(my_list)

print(my_list.pop()) # sale el ultimo
print(my_list)

my_pop_element = my_list.pop(2) # guarda el elemento con indice 2 en my_pop_element
print(my_pop_element) 
print(my_list)

del my_list[2] # eimina el valor con indice 2
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)


my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)