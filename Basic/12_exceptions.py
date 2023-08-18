### Exception Handling ###

numberOne, numberTwo = 5, 1

numberTwo = "1"

# try except

try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except:
    print("Se ha producido un error")

# try except else finally

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except: #obligatorio
    print("Se ha producido un error")
else:  # Opcional
    # Se ejecuta si no se produce una excepción (error)
    print("La ejecución continúa correctamente")
finally:  # Opcional
    # Se ejecuta siempre
    print("La ejecución continúa")

# Excepciones por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except TypeError:
    print("Se ha producido un TypeError")
except ValueError:
    print("Se ha producido un ValueError")


# Captura de la info de la excepcion 

try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
