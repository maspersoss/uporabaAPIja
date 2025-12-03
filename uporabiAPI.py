#Najdi državo z največ prebivalci
import requests
"""

url = "https://restcountries.com/v3.1/all?fields=name,population"

klic = requests.get(url).json()
maxPreb = 0
maxPrebIme = ""
minPreb = float("inf")
minPrebIme = ""

for k in klic:
    ime = k["name"]["common"]
    pop = k["population"]

    if pop > maxPreb:
        maxPreb = pop
        maxPrebIme = ime
    elif pop < minPreb and pop != 0:
        minPreb = pop
        minPrebIme = ime


print(maxPrebIme, maxPreb)
print("--------------------")
print(minPrebIme, minPreb)
"""

def sesta():
    #6. Izpiši št. držav, ki imajo za uradni jezik angleščino
    url = "https://restcountries.com/v3.1/all?fields=name,languages"

    klic = requests.get(url).json()
    lang = ""
    stDrzav = 0

    for k in klic:

        lang = k["languages"]

        if "eng" in lang:
            stDrzav += 1

    print(stDrzav)


def deveta():
    #9. Katera država ima najdaljše ime

    url = "https://restcountries.com/v3.1/all?fields=name"

    klic = requests.get(url).json()
    ime = ""
    lenImena = 0


    for k in klic:

        if len(k["name"]) > lenImena:
            lenImena = len(k["name"]["official"])
            ime = k["name"]["official"]


    print(ime, lenImena)

def prva():
    #1. Poišči državo z največ sosedi (borders)

    url = "https://restcountries.com/v3.1/all?fields=name,borders"

    klic = requests.get(url).json()
    stSosedov = 0
    ime = ""

    for k in klic:

        if "borders" in k and len(k["borders"]) > stSosedov:
            stSosedov = len(k["borders"])
            ime = k["name"]["common"]

    print(ime, stSosedov)





sesta()
deveta()
prva()