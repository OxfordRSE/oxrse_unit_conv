import unittest
from oxrse_unit_conv.units import ft2, m2


class TestSqFeet(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(ft2.si_unit.matches(m2))

    def test_basic_conversion(self):
        self.assertEqual(ft2.to_si(1), 0.092903)
        self.assertEqual(m2.to_unit(1, ft2), 1/0.092903)


if __name__ == '__main__':
    unittest.main()
