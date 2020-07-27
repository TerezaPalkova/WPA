
def mena(meno):
    if meno[0] in ["A", "e", "i", "o", "u", "a", "E", "I", "O", "U"]:
        return True
    else:
        return False

if __name__ == "__main__":
    meno = mena("Adam")
    if meno == True:
             print(f"Meno: zacina samohlaskou")
    else:
        print(f"Meno: zacina spoluhlaskou")