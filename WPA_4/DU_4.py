import random


def matrix_generator(rows, columns, min_value, max_value):
    """ Vygeneruje maticu rows x columns s hodnotami min_value .. max_value
    :param rows: int
    :param columns: int
    :param min_value: int
    :param max_value: int
    :return: list (matica rows x columns of int)
    """
    komplet_data = []
    for i in range(rows):
        vnutorne_data = []
        for y in range(columns):
            cislo = random.randint(min_value, max_value+1)
            vnutorne_data.append(cislo)
        komplet_data.append(vnutorne_data)
    return komplet_data


    rows = int(input("Zadaj pocet riadkov: "))
    cols = int(input("Zadaj pocet stlpcov: "))
    minimal = int(input("Zadaj min: "))
    maximal = int(input("Zadaj max: "))

matrix = matrix_generator(rows, cols, minimal, maximal)
print(matrix)
