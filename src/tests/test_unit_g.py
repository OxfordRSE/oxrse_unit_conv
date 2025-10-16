import unittest
from oxrse_unit_conv.units import g, kg


class TestPound(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(g.si_unit.matches(kg))

    def test_basic_conversion(self):
        self.assertEqual(g.to_si(1), 0.001)
        self.assertEqual(g.to_unit(1000, g), 1000)


if __name__ == '__main__':
    unittest.main()
