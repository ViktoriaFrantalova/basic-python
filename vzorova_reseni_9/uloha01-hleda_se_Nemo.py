"""
Úloha:
Vytvořte program, který načte soubor CSFD-Hleda_se_Nemo.txt 
a vypíše na výstup všechny řádky, na kterých se vyskytuje slovo Nemo. 
Navyše bude u každého řádku uvedené pořadí řádku v původním souboru.
Pozor: zvolte správné kódování, aby se podařilo soubor načíst 
a aby se správně zobrazila diakritika.

Vzorový výstup:  
   2 a odlehlém příbytku ze sasanek Marlin a jeho jediný syn Nemo. Marlin se s
   4 snaží svého syna před nástrahami okolí ochránit. Nemo je však, stejně jako
  23 postaviček. Scénáristou a režisérem filmu Hledá se Nemo je Andrew Stanton,
  27 Hledá se Nemo a jeho úžasný podmořský svět je zcela novým uměleckým a
"""

soubor = 'CSFD-Hleda_se_Nemo.txt'
hledane_slovo = 'Nemo'

with open(soubor, encoding='cp1250') as f:
    for i, radek in enumerate(f, 1):
        if hledane_slovo in radek:
            print(f'{i:>4} {radek.strip()}')
