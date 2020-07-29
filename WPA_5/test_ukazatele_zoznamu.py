from unittest import TestCase
from WPA_5.work_with_numbers import ukazatele_zoznamu

data = (10, 8, 64, 100,12,-5)
class TestUkazatele_zoznamu(TestCase):
    def test_ukazatele_zoznamu(self):
        d = ukazatele_zoznamu(data)
        self.assertIsInstance(d, dict)

    def test_ukazatele_zoznamu_min(self):
        d = ukazatele_zoznamu(data)
        self.assertEqual(min(data), -5)

    def test_ukazatele_zoznamu_max(self):
        d = ukazatele_zoznamu(data)
        self.assertEqual(max(data), 100)

    def test_ukazatele_zoznamu_sum(self):
        d = ukazatele_zoznamu(data)
        self.assertEqual(sum(data), 189)


