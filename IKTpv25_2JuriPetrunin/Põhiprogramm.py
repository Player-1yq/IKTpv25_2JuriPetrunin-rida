
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
        os.mkdir(nimi)
        return True
    return False
#Ülesanne 4

def leia_failid_algustahega(taht):
    return glob.glob(f"{taht}*.*")

def taisanaluus(laiend):
    failid = leia_projektifailid(laiend)
    kogusuurus = 0

    for f in failid:
        if os.path.isfile(f):
            kogusuurus += os.path.getsize(f)

    print(f"\nAnalüüs laiendile {laiend}:")
    print(f"Failide arv: {len(failid)}")
    print(f"Kogusuurus: {kogusuurus} baiti")

    return len(failid), kogusuurus

#teine osa

def puhasta_logid():
    kaust = "Analüüsi_Raportid"
    if not os.path.exists(kaust):
        print("Raporteid ei leitud.")
        return

    puhasta = input("Kas kustutada kõik raportid? (j/e): ")
    if puhasta.lower() == "j":
        for f in os.listdir(kaust):
            os.remove(os.path.join(kaust, f))
        print("Raportid kustutatud.")
    else:
        print("Kustutamine katkestatud.")
def main():
    print("")
    for f in os.listdir():
        if os.path.isfile(f):
            print(os.path.splitext(f)[1])

    valik_stat = None
