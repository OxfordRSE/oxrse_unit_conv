import unittest
from oxrse_unit_conv.units import cm, m


class TestCentimetre(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(cm.si_unit.matches(m))

    def test_to_si(self):
        self.assertEqual(cm.to_si(1), 0.1)



if __name__ == '__main__':
    unittest.main()