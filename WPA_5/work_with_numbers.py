# work_with_numbers.py.py

# Zadávam celé čísla ako vstup programu z klávesnice. Zadávanie končím prázdnym riadkom.
# Program mi na výstupe zobrazí:
#
#
# pocet: x | spolu: y | priemer: z | najmensie: a | najvacsie: b


def pridavaj_cisla():
    return_value = []
    cislo = input("Zadaj cislo alebo enter: ")
    while cislo:
        if cislo.isnumeric():
            cislo = int(cislo)
            return_value.append(cislo)
            cislo = input("Zadaj cislo alebo enter: ")
        else:
            raise TypeError("Zadane cislo nieje int")
    return return_value


def ukazatele_zoznamu(data):
    # TU treba napisat testy
    # aspon 3-4 testy
    for i in data:
        if isinstance(i, int):
            continue
        else:
            raise TypeError(f"Cislo {i} zo zoznamu {data} nie je int")
    d = dict()
    d["min"] = min(data)
    d["max"] = max(data)
    d["priemer"] = sum(data) / len(data)
    d["spolu"] = sum(data)
    d["pocet"] = len(data)
    return d


if __name__ == "__main__":
    zoznam_cisel = pridavaj_cisla()
    result = ukazatele_zoznamu(zoznam_cisel)

    print(f"pocet: {result['pocet']} | spolu: {result['spolu']} |"
          f" priemer: {result['priemer']} | najmensie: {result['min']} | najvacsie: {result['max']}")