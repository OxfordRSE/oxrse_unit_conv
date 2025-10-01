from oxrse_unit_conv.si import *
from oxrse_unit_conv.meta.classes import Unit

# second
minute = Unit(name='minute', abbr='min', si=second, to_si_fun=lambda n: n * 60)
# min shadows the builtin function 'min'

hour = Unit(name='hour', abbr='h', si=second, to_si_fun=lambda n: n * 3600)
h = hour

# meter
kilometer = Unit(name='kilometer', abbr="km", si=meter, to_si_fun=lambda n: n * 1000)
km = kilometer

mile = Unit(name='mile', abbr='mile', si=meter, to_si_fun=lambda n: n * 1_609.344)

# meter_sq

centremeters_sq = Unit(name='centremeters_sq', abbr='cm2', si=meter_sq, to_si_fun=lambda n: n / 10000)
cm2 = centremeters_sq

feet_sq = Unit(name='feet_sq', abbr='ft2', si=meter_sq, to_si_fun=lambda n: n / 10.764)
ft2 = feet_sq

# meter_cu

# kilogram

pound = Unit(name='pound', abbr='lb', si=kilogram, to_si_fun=lambda n: n * 0.4535924)
lb = pound

# ampere

# kelvin

# mole

# candela
