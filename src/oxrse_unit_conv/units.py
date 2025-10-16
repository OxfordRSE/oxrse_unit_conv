from si import *
from meta.classes import Unit

# second
minute = Unit(name='minute', abbr='min', si=second, to_si_fun=lambda n: n * 60)
# min shadows the builtin function 'min'
minutes = minute

hour = Unit(name='hour', abbr='h', si=second, to_si_fun=lambda n: n * 3600)
h = hour
hr = hour
hrs = hour
hours = hour

# meter
kilometer = Unit(name='kilometer', abbr="km", si=meter, to_si_fun=lambda n: n * 1000)
km = kilometer
kms = kilometer
kilometers = kilometer
mile = Unit(name='mile', abbr='mi', si=meter, to_si_fun=lambda n: n * 1_609.344)
mi = mile
miles = mi

# meter_sq

# meter_cu

# kilogram
gram = Unit(name='gram', abbr='g', si=kilogram, to_si_fun=lambda n: n / 1000)
g = gram
grams = gram
pound = Unit(name='pound', abbr='lb', si=kilogram, to_si_fun=lambda n: n * 0.4535924)
lb = pound
lbs = pound
pounds = pound

# ampere

# kelvin
celsius = Unit(name="celsius", abbr="C", si=kelvin, to_si_fun=lambda n: n + 273.15)
C = celsius
fahrenheit = Unit(name="fahrenheit", abbr="F", si=kelvin, to_si_fun=lambda n: ((n-32)/1.8) + 273.15)
F = fahrenheit

# mole

# candela
