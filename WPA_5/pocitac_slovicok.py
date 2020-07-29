import urllib.request
import ssl
from collections import Counter


def load_data(url):
    gcontext = ssl.SSLContext()
    data = str(
        urllib.request.urlopen(
            url,
            context=gcontext).read().decode("utf-8")
    )
    return data


def count_words(data, pismena=True):
    # napisat testy
    # aspon 3-4 testy
    if not pismena:
        data = data.split(" ")
    znaky = Counter(data)
    return znaky


if __name__ == "__main__":
    link = "https://raw.githubusercontent.com/tomaspekarovic/PythonAcademy/master/Lekcia5/random_text.txt"
    data_na_spracovanie = load_data(link)
    vysledny_slovnik = count_words(data_na_spracovanie, pismena=False)
    print(vysledny_slovnik)