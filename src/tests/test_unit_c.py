import unittest
from oxrse_unit_conv.units import C, K


class TestKilometer(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(C.si_unit.matches(K))

    def test_basic_conversion(self):
        self.assertEqual(C.to_si(1), 273.15)
        self.assertEqual(C.to_unit(10, C), 10)


if __name__ == '__main__':
    unittest.main()
