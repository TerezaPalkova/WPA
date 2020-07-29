
def mena(meno):
    meno=str(meno)
    if meno[0] in ["A", "e", "i", "o", "u", "a", "E", "I", "O", "U"]:
        return True
    else:
        return False

if __name__ == "__main__":
    meno = mena(7)
    if meno is True:
             print(f"Meno: zacina samohlaskou")
    else:
        print(f"Meno: zacina spoluhlaskou")



def pyramida (zakladna,smer,centrovanie):
    """
        Funkcia pyramida.

        Parametre:
        1.argument (int): velkost zakladne
        2.argument (str): smer pyramidy
            "normalna"
            "obratena"
        3.argument (str): centrovanie pyramidy
            "center"
            "vlavo"

        """
    for h in range(zakladna):
        if centrovanie== "center":
           if smer == "obratena":
               if h%2 != 0:
                    print(list(str("*" * (zakladna - h)).center(zakladna)))


           elif smer == "normalna":
                if h % 2 == 0:
                    print(list(str("*" * (h + 1)).center(zakladna)))

           else:
               print (f"Zadali ste zly udaj na druhom mieste. Prosim upravte slovo {smer}")
               break

        elif centrovanie == "vlavo":
           if smer == "obratena":
                 print(list("*"*(zakladna-h)))
           else:
                 print(list("*" * (h + 1)))
                 h += 1
        else:
            print(f"Zadali ste zly udaj na tretom mieste. Prosim upravte slovo {centrovanie}")
            break

if __name__ == "__main__":
 pyramida(10, "normalna","center")