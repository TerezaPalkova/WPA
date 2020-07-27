from unittest import TestCase


class TestMatrix_generator(TestCase):
    def test_matrix_generator(self):
        result = leapyear(2000)   # True
        self.assertTrue(result)
