### Modules ###

import my_module

my_module.sum(5, 3, 1)
my_module.printValue("Hola Python!")

from my_module import sum, printValue

sum(5, 3, 1)
printValue("Hola Python!")

import math

print(math.pi)
print(math.pow(2, 8))

from math import pi as PI_VALUE

print(PI_VALUE)