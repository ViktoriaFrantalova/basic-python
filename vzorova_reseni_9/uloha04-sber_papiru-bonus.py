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

from collections import defaultdict


papir = defaultdict(lambda: 0.0)

# lambda funkce -> kapitola 6 - rozšiřující učivo

# defaultdict -> 
# https://www.accelebrate.com/blog/using-defaultdict-python
# https://docs.python.org/3.7/library/collections.html#defaultdict-objects

with open('papir.txt') as r:
    r.readline()  # Ignorujeme 1. řádek
    for line in r:
        datum, jmeno, mnozstvi = line.strip().split(',')
        jmeno = jmeno.strip()
        mnozstvi = float(mnozstvi)
        papir[jmeno] += mnozstvi  # Pokud jmeno není ve slovníku papír, tak se automaticky přidá, protože je to defaultdict.

for jmeno, mnozstvi in sorted(papir.items(), key = (lambda item: item[1]), reverse=True):
    print(f'{jmeno}: {mnozstvi}')       
