import urllib.request
import ssl

gcontext = ssl.SSLContext()
data = str(
    urllib.request.urlopen(
        "https://raw.githubusercontent.com/tomaspekarovic/PythonAcademy/master/Lekcia5/random_file.txt",
        context=gcontext).read().decode("utf-8")
)

# data = str(
# urllib.request.urlopen(
# "https://raw.githubusercontent.com/tomaspekarovic/PythonAcademy/master/Lekcia5/random_text.txt",
# context=gcontext).read().decode("utf-8")
#

dat =list(data)
import pandas as pd


df = pd.DataFrame (dat,columns=["data"])
print (df["data"].value_counts(ascending=False))
print(df.head())


zoz=[]
def praca_s_cislami():
     while p:
         if isinstance(p, int):
            p =(input("vloz cislo:"))
            zoz.append(p)
         else:
             raise TypeError("nie je to integer")
     return zoz



l=[1,3,6,7]

def stastic(l):
    print(len(l))
    print(sum(l))
    print(sum(l) / len(l))
    print(min (l))
    print(max (l))

stastic(l)