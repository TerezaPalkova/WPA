import time
import turtle
import math


def domcek (d):
    for x in range(4):
        d.forward(200)
        d.left(90)
    d.left(45)
    d.forward(math.sqrt(((200**2)*2)))
    d.left(90)
    d.forward((math.sqrt(((200**2)*2))/2))
    d.left(90)
    d.forward((math.sqrt(((200**2)*2))/2))
    d.left(90)
    d.forward(math.sqrt((200**2)*2))
#t=turtle.Turtle()

#domcek(t)
time.sleep(2)

#domaca uloha

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
                    print (str("*" * (zakladna - h)).center(zakladna))

           elif smer == "normalna":
                if h % 2 == 0:
                    print(str("*" * (h + 1)).center(zakladna))
           else:
               print (f"Zadali ste zly udaj na druhom mieste. Prosim upravte slovo {smer}")
               break

        elif centrovanie == "vlavo":
           if smer == "obratena":
                 print("*"*(zakladna-h))
           else:
                 print("*" * (h + 1))
                 h += 1
        else:
            print(f"Zadali ste zly udaj na tretom mieste. Prosim upravte slovo {centrovanie}")
            break


pyramida(10, "normalna","center")

print (pyramida.__doc__)


#