from unittest import TestCase
from DU_4 import matrix_generator


class TestMatrix_generator(TestCase):
    def test_matrix_generator(self):
        result = leapyear(2000)   # True
        self.assertTrue(result)
