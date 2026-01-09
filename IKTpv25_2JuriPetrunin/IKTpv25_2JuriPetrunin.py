#def loe_failist(failinimi):
#    """Loeb faili ja tagastab sellee sisu listine"""
#    loend=[]
#    try:
#        with open(failinimi+".txt","r", encoding="utf-8") as f:
#            for rida in f:
#                loend.append(rida.strip())
#    except FileNotFoundError:
#        print(f"Viga! Faili {failinimi}.txt ei leitud")
#    return loend

#def kirjuta_faili(failinimi:str, loend:list):
#    """Kirjutab listi sisu faili"""
#    try:
#        rezlim=input("Kas soovid üle kirjutada -w- või lisada -a-: ")
#        if rezlim not in ["w", "a"]:
#            raise ValueError("Viga! palun sisesta 'w' või 'a'. ")
#    except ValueError as ve:
#        print(ve)

#    with open(failinimi+".txt","w", encoding="utf-8") as f:
#        for rida in loend:
#            f.write(rida+"\n")

#nimekiri=[]
#for i in range(5):
#    nimi=input(f"Sisesta {i+1}. nimi: ")
#    nimekiri.append(nimi)

#failinimi=input("Sisesta faili nimi ilma laiendita, kuhu buned salvestada: ")
#kirjuta_faili(failinimi, nimekiri)

#failinimi=(input("Sisesta faili nimi ilma laiendita: "))
#päevad=loe_failist(failinimi)
#print("Faili sisu read on: ")
#for rida in päevad:
#    print(rida)
#print("Faili sisu listina: ")
#print(päevad)



#import os
#f = open('rida.txt', 'r')
#print(dir(f)) # Kuvab kõik failiobjekti meetodid (nt. read, close)
#f.close()
#praeguse_kataloog=os.getcwd()
#print(f"{praeguse_kataloog}")
#praeguse_kataloog=os.listdir()
#print(f"")
#praeguse_karaloog=os.path.exists('rida.txt')
#print(f"{praeguse_kataloog}")



import glob
import os
from datetime import datetime

f = open('rida.txt', 'r')
print(dir(f))
f.close()

def leia_projektifailid(laiend, asukoht="."):
    if not laiend.startswith("."):
        laiend = "." + laiend
    return glob.glob(f"*{laiend}")
    asukoht = input("Sisesta kataloogi asukoht (tühjaks jätmisel kasutatakse praegust asukohta): ")
    muster = os.path.join(asukoht, f"*{laiend}")
    failid= glob.glob(muster)
    return failid

failid1 = leia_projektifailid(".py")

failid2 = leia_projektifailid(".txt", "Analüüsi_Raportid")

failid3 = leia_projektifailid(".csv", "C:rida/Desktop/Andmed")

print("Leitud .py failid: ", failid1)
print("Leitud .txt failid Analüüsi_Raportid kasutas: ", failid2)
print("Leitud .csv failid C:rida/Desktop/Andmed kasutas: ", failid3)

#Ülesanne 3
def loo_raporti_kataloog(nimi="Analüüsi_Raportid"):
    if not os.path.exists(nimi):
        os.midir(nimi)
        return True
    return False
#Ülesanne 4
def leia_failid_algustahega(taht):
    return glob.glob(f"{taht}*.*")
