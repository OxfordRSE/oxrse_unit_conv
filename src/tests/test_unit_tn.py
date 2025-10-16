import unittest
from oxrse_unit_conv.units import tn, kg


class TestTonne(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(tn.si_unit.matches(kg))

    def test_basic_conversion(self):
        self.assertEqual(tn.to_si(1), 1000)
        self.assertAlmostEqual(tn.to_unit(1, tn), 1, 1e-3)


if __name__ == '__main__':
    unittest.main()
