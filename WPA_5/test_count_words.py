from unittest import TestCase
from WPA_5.pocitac_slovicok import  count_words

data= "jahoda jablko les 4555 */* dom"
class TestCount_words(TestCase):
    def test_count_words_dict(self):
        znaky = count_words(data,pismena=True)
        self.assertIsInstance(znaky, dict)

    def test_count_words_len_words(self):
        znaky = count_words(data, pismena=False)
        self.assertEqual(len(znaky), 6)

    def test_count_words_len_letters(self):
        znaky = count_words(data, pismena=True)
        self.assertEqual(len(znaky), 16)


