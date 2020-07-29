#pyramida 1
zoz=[1,2,3,4,5,6,7,8,9,10]

for n in zoz :
    print("*"* n)
    n+=1


#pyramida 2
l=9
for h in range(10):
    print("*"*(l+1))
    l-=1

#pyramida 2 (bez extra premennej)
for h in range (10):
    # krasne zlozity vypocet.
    # print("*"*(10-h))
    print("*"*((h+10)-2*h))


#prestupny rok
year= int(input("Choose a year:" ))

if ((year % 4 == 0) and (year % 100 != 0)) or ((year % 4 == 0) and (year % 400 == 0)) :
    print (f"rok {year} je prestupny")
else:
    print (f"rok{year} je neprestupny")

# prestupny rok range
years= range(2000,2002)
# v zadani bolo, ze rok chceme 2 inputy.. ale v zasade je to v poriadku
for year in years:
    # Ak je rok delitelny 400 , tak musi byt aj 4
    # takze podmienka ide este zjednodusit
    # if ((year % 4 == 0) and (year % 100 != 0)) or year % 400 == 0:
    if ((year % 4 == 0) and (year % 100 != 0)) or ((year % 4 == 0) and (year % 400 == 0)) :
       print(f"rok {year} je prestupny")
    else:
        print(f"rok {year} je neprestupny")

