import unittest
from oxrse_unit_conv.units import d, s

class TestDay(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(d.si_unit.matches(s))

    def test_basic_conversion(self):
        self.assertEqual(d.to_si(1), 86_400)
        self.assertEqual(d.to_unit(10, d), 10)

if __name__ == '__main__':
    unittest.main()