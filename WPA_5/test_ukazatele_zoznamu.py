from unittest import TestCase
from WPA_5.work_with_numbers import ukazatele_zoznamu


class TestUkazatele_zoznamu(TestCase):
    def test_ukazatele_zoznamu(self):
        result = ukazatele_zoznamu(10, 8, 64, 100)
        self.assertIsInstance(result, touple)

    def test_ukazatele_zoznamu(self):
        result = ukazatele_zoznamu(10, 8, 64, 100)
        self.assertEqual(min(result), 8)

    def test_ukazatele_zoznamu(self):
        result = ukazatele_zoznamu(10, 8, 64, 100)
        self.assertEqual(max(result), 100)

    def test_ukazatele_zoznamu(self):
        result = ukazatele_zoznamu(10, 8, 64, 100)
        self.assertEqual(sum(result), 182)




