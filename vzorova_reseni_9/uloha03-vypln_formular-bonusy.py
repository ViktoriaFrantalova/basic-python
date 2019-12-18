"""
Úloha:
Vytvořte program, který bude načítat soubor formular.txt a postupne ho 
vypisovat na standardní výstup. Na každém řádku končícím dvojtečkou se 
výpis zastaví a od uživatele (tj. ze standardního vstupu) se načte 
potřebný údaj. Formulář s doplněnými údaji se uloží do souboru 
formular-vyplneny.txt. Příkladem výstupního souboru je formular-vyplneny-vzor.txt.

Bonus: 
Modifikujte program tak, aby umožnil uživateli zadat název 
vstupního a výstupního souboru. Pokud výstupní soubor už existuje, zeptá se 
program uživatele, jestli chce tento soubor přepsat.

Bonus2: 
Na konec vytvořeného souboru doplňte automaticky datum vyplnění.
"""

from os import path
import datetime


vstupni_soubor = input('Vstupní soubor: ')
vystupni_soubor = input('Výstupní soubor: ')
if path.exists(vystupni_soubor):
    prepsat = input(f'Soubor {vystupni_soubor} už existuje. Chcete ho prepsat? (ano/ne)')
    if prepsat != 'ano':
        exit()

with open(vstupni_soubor, encoding='utf8') as fr:
    with open(vystupni_soubor, 'w', encoding='utf8') as fw:
        for radek in fr:
            radek = radek.rstrip('\r\n')  # Odstraníme pouze znaky nového řádku, ne mezery
            if radek.strip().endswith(':'):
                # Načítáme hodnotu od uživatele
                print(radek, end='')
                hodnota = input()
                fw.write(f'{radek}{hodnota}\n')
            else:
                # Pouze zkopírujeme řádek do výstupního souboru
                fw.write(f'{radek}\n')
        datum = datetime.datetime.now().date()
        fw.write(datum.strftime('Datum: %d. %m. %Y\n'))        
