def loe_failist(failinimi):
    """Loeb faili ja tagastab sellee sisu listine"""
    loend=[]
    try:
        with open(failinimi+".txt","r", encoding="utf-8") as f:
            for rida in f:
                loend.append(rida.strip())
    except FileNotFoundError:
        print(f"Viga! Faili {failinimi}.txt ei leitud")
    return loend

def kirjuta_faili(failinimi:str, loend:list):
    """Kirjutab listi sisu faili"""
    try:
        rezlim=input("Kas soovid üle kirjutada -w- või lisada -a-: ")
        if rezlim not in ["w", "a"]:
            raise ValueError("Viga! palun sisesta 'w' või 'a'. ")
    except ValueError as ve:
        print(ve)

    with open(failinimi+".txt","w", encoding="utf-8") as f:
        for rida in loend:
            f.write(rida+"\n")

nimekiri=[]
for i in range(5):
    nimi=input(f"Sisesta {i+1}. nimi: ")
    nimekiri.append(nimi)

failinimi=input("Sisesta faili nimi ilma laiendita, kuhu buned salvestada: ")
kirjuta_faili(failinimi, nimekiri)

failinimi=(input("Sisesta faili nimi ilma laiendita: "))
päevad=loe_failist(failinimi)
print("Faili sisu read on: ")
for rida in päevad:
    print(rida)
print("Faili sisu listina: ")
print(päevad)
