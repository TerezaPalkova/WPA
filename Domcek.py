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
t=turtle.Turtle()

domcek(t)
time.sleep(2)

#domaca uloha

def pyramida (zakladna,smer,centrovanie):
    for h in range(zakladna):
        if centrovanie== "center":
           if smer == "obratena":
              print(str("*"*(zakladna-h)).center(2*zakladna)) #neviem kde robim chybu, ze mi to centruje tak zvlastne
           else:
              print(str("*" * (h + 1)).center(2*zakladna))
              h+=1
        else:
           if smer == "obratena":
              print("*"*(zakladna-h))
           else:
              print("*" * (h + 1))
              h += 1

pyramida(10, "obratena","center")


