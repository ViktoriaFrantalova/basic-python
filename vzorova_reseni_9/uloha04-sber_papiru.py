"""
Úloha:
Soubor papir.txt obsahuje informace o sběru papíru - kdy, kdo, a kolik kg donesl.
Napište program, který načte tento soubor a spočítá celkovou hmotnost sesbíraného 
papíru pro každou osobu. Výsledek vypíše na standardní výstup, osoby budou seřazeny 
podle abecedy.

Vzorový výstup:  
Alice: 15.0
Bob: 28.0
Cyril: 19.5
Dana: 20.0
Emil: 7.5
Filip: 8.0
Gertruda: 24.0
Hanka: 27.5
Ivan: 20.0
John: 22.0

Bonus: 
Modifikujte program tak, aby vypisoval lidi v pořadí podle nasbíraného množství papíru (od největšího po nejmenší).
"""

papir = {}

with open('papir.txt') as r:
    r.readline()  # Ignorujeme 1. řádek
    for line in r:
        datum, jmeno, mnozstvi = line.strip().split(',')
        jmeno = jmeno.strip()
        mnozstvi = float(mnozstvi)
        if jmeno not in papir:
            papir[jmeno] = 0.0
        papir[jmeno] += mnozstvi

for jmeno, mnozstvi in sorted(papir.items()):
    print(f'{jmeno}: {mnozstvi}')
