### Classes ###

# Definición

class MyEmptyPerson:
    pass  # Para poder dejar la clase vacía

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname):
        self.full_name = f"{name} {surname}"

    def walk(self):
        print(f"{self.full_name} está caminando")
        

my_person = Person("Ariel", "Tapia")
print(my_person.full_name)
my_person.walk()