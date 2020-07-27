from unittest import TestCase
from Blbosti.WPA_4 import leapyear


class TestLeapyear(TestCase):
    def test_leapyear_true_2000(self):
        result = leapyear(2000)  # True
        self.assertTrue(result)

    def test_leapyear_true_2004(self):
        result = leapyear(2004)  # True
        self.assertTrue(result)

    def test_leapyear_false_2001(self):
        result = leapyear(2001)  # False
        self.assertFalse(result)

    def test_leapyear_false_2100(self):
        result = leapyear(2100)  # False
        self.assertFalse(result)

    def test_leapyear_string(self):
        result = leapyear("dfahh")  # False
        self.assertFalse(result)



