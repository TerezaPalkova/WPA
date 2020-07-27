from unittest import TestCase
from DU_4_mena import mena


class TestMena(TestCase):
    def test_mena_samohlaska(self):
        meno = mena("Adam")  # True
        self.assertTrue(meno)

    def test_mena_spoluhlaska(self):
        meno = mena("Tomas")  # false
        self.assertFalse(meno)

    def test_mena_cislo(self):
        meno = mena("7")  # false
        self.assertFalse(meno)

    def test_mena_list(self):
        meno = mena([1,2])  # false
        self.assertFalse(meno)

    def test_mena_tuple(self):
        meno = mena((1,2))  # false
        self.assertFalse(meno)

    def test_mena_znak(self):
        meno = mena("*")  # false
        self.assertFalse(meno)

