"""
Úlaha:
Napište program, který načte soubor ve formátu CSV, spočítá statistiku 
z každého sloupce a výsledek uloží do výstupního CSV souboru.
Uživatel zadá název vstupního a výstupního souboru z příkazové řádky. 
Dále může uživatel zadat:
- že první řádek tabulky ve vstupním souboru se má brát jako hlavička 
a tato hlavička se má vypsat i do výstupního souboru (pomocí --header)
- jaký je oddělovač ve vstupním a výstupním souboru (pomocí --delimiter)
- jaký typ statistiky (průměr/medián/min/max) se má počítat (pomocí --stat)

Pokud se některé hodnoty v sloupci nepodaří převést na číslo, nechte 
buňku odpovídající tomuto sloupci ve výstupní tabulce prázdnou.

Příklady spuštění z příkazové řádky:
$ python3  uloha03-statistika.py  tabulka1.csv  vystup1.csv  --stat median  --header  --delimiter ";"
$ python3  uloha03-statistika.py  tabulka2.csv  vystup2.csv  --stat max

(Všimněte si, že znak středník musí být v uvozovkách. To proto, že některé 
znaky (; | < > ? * mezera atd.) jsou speciální znaky příkazové řádky (tj. bashu 
nebo powershellu). Aby se jejich speciální funkce zrušila, zadáme je do příkazové 
řádky v uvozovkách. Tyto uvozovky se automaticky odstraní, tj. zadáme-li 
napr. ";", tak Python dostane už jen jeden znak - středník.)

Vzorové výstupní soubory jsou vystup1-vzor.csv, vystup2-vzor.csv.
"""

import argparse
import csv
from typing import List, Optional
import statistics


def nacti_argumenty():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Input CSV file', type=str)
    parser.add_argument('output', help='Output CSV file', type=str)
    parser.add_argument('-H', '--header', help='Interpret the first line as column names', action='store_true')
    parser.add_argument('-d', '--delimiter', help='Delimiter in the CSV files', type=str, default=',')
    parser.add_argument('-s', '--stat', help='Type of statistic to be computed', choices=['mean', 'median', 'min', 'max'], default='mean')
    arguments = parser.parse_args()
    return arguments

def extrahuj_sloupce(tabulka: List[List[str]]) -> List[List[float]]:
    """
    Předělej tabulku ze seznamu řádků na seznam sloupců a konvertuj hodnoty na float.
    Pokud některé hodnoty ve sloupci nelze převést na float, vlož místo tohoto sloupce [].
    """
    n_sloupcu = len(tabulka[0])
    sloupce = []
    for i in range(n_sloupcu):
        try:
            novy_sloupec = [float(radek[i]) for radek in tabulka]
        except ValueError:  # Pokud se některou hodnotu nepodaří konvertovat na float
            novy_sloupec = []
        sloupce.append(novy_sloupec)
    return sloupce

def spocitej_statistiku(typ_statistiky: str, hodnoty: List[float]) -> Optional[float]:  # Optional[float] znamená float nebo None
    """Spočítej požadovanou statistiku (mean/median/max/min) pro seznam hodnot. Vrať None, pokud je seznam prázdný."""
    if len(hodnoty) == 0:
        return None
    elif typ_statistiky == 'mean':
        return statistics.mean(hodnoty)
    elif typ_statistiky == 'median':
        return statistics.median(hodnoty)
    elif typ_statistiky == 'min':
        return min(hodnoty)
    elif typ_statistiky == 'max':
        return max(hodnoty)
    else:
        raise ValueError(f'Neznámý typ statistiky: {typ_statistiky}')


args = nacti_argumenty()

with open(args.input, encoding='utf8') as f:
    reader = csv.reader(f, delimiter=args.delimiter)
    tabulka = list(reader)
        
if args.header:
    hlavicka, *tabulka = tabulka

sloupce = extrahuj_sloupce(tabulka)

statistiky = []
for sloupec in sloupce:
    statistika = spocitej_statistiku(args.stat, sloupec)
    statistiky.append(statistika)

with open(args.output, 'w', encoding='utf8') as f:
    writer = csv.writer(f, delimiter = args.delimiter)
    if args.header:
        writer.writerow(hlavicka)
    writer.writerow(statistiky)
