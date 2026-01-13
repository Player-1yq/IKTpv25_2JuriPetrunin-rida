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


import os
from Põhiprogramm import *

from Põhiprogramm import leia_projektifailid
while True:
    print("-"*20)
    print("""
1 - Täisanalüüs
2 - Salvesta raport
3 - Puhasta logid
4 - Otsi faili algustähe järgi
0 - Välju
""")
    print("-"*20)
    valik = input("Valige tegevus, mida te tahate teha: ")
    if valik == "1":
        laiend = input("Sisesta faililaiend (nt .py): ")
        valik_stat = taisanaluus(laiend)

       # elif valik == "2":
       #     if viimane_stat:
       #         salvesta_raport(viimane_stat)
       #     else:
       #         print("Kõigepealt tee analüüs!")
    elif valik == "3":
        puhasta_logid()

    elif valik == "4":
        taht = input("Sisesta algustäht: ")
        failid = leia_failid_algustahega(taht)
        print("Leitud failid:")
        print("-"*20)
        for f in failid:
            print(f)

    elif valik == "0":
        kustuda = input("kas te soovite lõpetada? (j/e): ")
        if kustuda.lower() == "j":
            print("-"*20)
            print("Programm lõpetatud.")
            break
        else:
            continue

    else:
        print("Palun valige valik!")


if __name__ == "__main__":
    main()
