from si import *
from meta.classes import Unit

# second
minute = Unit(name='minute', abbr='min', si=second, to_si_fun=lambda n: n * 60)
# min shadows the builtin function 'min'

hour = Unit(name='hour', abbr='h', si=second, to_si_fun=lambda n: n * 3600)
h = hour

# meter
kilometer = Unit(name='kilometer', abbr="km", si=meter, to_si_fun=lambda n: n * 1000)
km = kilometer

centimeter = Unit(name='centimeter', abbr='cm',si=meter, to_si_fun=lambda n: n / 100)
cm = centimeter


mile = Unit(name='mile', abbr='mile', si=meter, to_si_fun=lambda n: n * 1_609.344)

# meter_sq

# meter_cu

# kilogram

pound = Unit(name='pound', abbr='lb', si=kilogram, to_si_fun=lambda n: n * 0.4535924)
lb = pound

# ampere

# kelvin

# mole

# candela


class TestCentimeter(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(cm.si_unit.matches(m))

    def test_basic_conversion(self):
        self.assertEqual(cm.to_si(1), 1_000)
        self.assertEqual(cm.to_unit(10, cm), 10)


if __name__ == '__main__':
    unittest.main()

TestCentimeter()