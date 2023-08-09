# sets

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # nos dice q inicialmente es un diccionario

my_other_set = {"Ariel", "Tapia", 31}
print(type(my_other_set)) # pero aqui ya es un set

print(len(my_other_set))

my_other_set.add("Artavi")

print(my_other_set) # un set no es una estructura ordenada 

my_other_set.add("Artavi") # un set no admite repetido 

print(my_other_set) 

print("Artavi" in my_other_set)
print("ArtaviIIII" in my_other_set)

my_other_set.remove("Artavi")
print(my_other_set)

my_other_set.clear() # vacía el set
print(len(my_other_set))

del my_other_set # elimina el set
# print(my_other_set) # da error porq no existe

my_set = {"Ariel", "Tapia", 31}
my_list = list(my_set)
print(my_list)
print(my_list[0]) # esto es muy arriesgado 

my_other_set = {"PHP", ".NET", "Python"}

my_new_set= my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_list).union({"JavaScript", "C#"}))

print(my_new_set.difference(my_set))