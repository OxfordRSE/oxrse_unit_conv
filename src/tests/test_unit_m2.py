import unittest
from oxrse_unit_conv.units import m2, m


class TestSquaremeter(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(m2.si_unit.matches(m))

    def test_basic_conversion(self):
        self.assertEqual(m2.to_si(10), 1_00)
        self.assertEqual(m2.to_unit(10, m2), 10)


if __name__ == '__main__':
    unittest.main()
