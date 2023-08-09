### Dicttionaries ###

my_dict = dict() 
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Ariel", "Apellido":"Tapia", "Edad":31, 1:"Python"}

my_dict = {
    "Nombre":"Ariel", 
    "Apellido":"Tapia", 
    "Edad":31, 
    "Lenguajes":{"Python", "PHP", ".NET"},
    1:1.77
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Calle Artavi"
print(my_dict)

del my_dict["Calle"]
print(my_dict)

print("Ariel" in my_dict)
print("Apellido" in my_dict)