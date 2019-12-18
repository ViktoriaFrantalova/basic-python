# 2. (16 bodů) Napište definici funkce funkce2, která vezme jako parametr seznam celých čísel. Návratovou hodnotou funkce bude přefiltrovaný seznam obsahující pouze čísla dělitelná třemi nebo pěti.

from typing import Dict, List, Tuple
from pprint import pprint

import math

def funkce2(cisla: List[int]) -> List[int]:
    """Vyfiltruj pouze čísla dělitelná 3 nebo 5.
    >>> funkce2([7, 12, 35, 15, 45, 16, 18])
    [12, 35, 15, 45, 18]
    """
    #moje riesenie
    vysledok = []
    for i in range(0,len(cisla)):
        if(cisla[i] % 3 == 0) or (cisla[i] % 5 == 0):
            vysledok.append(cisla[i])
    return vysledok

    #vzorove riesenia
    # vysledek = []
    # for cislo in cisla:
    #     if cislo % 3 == 0 or cislo % 5 == 0:
    #         vysledek.append(cislo)
    # return vysledek
    #--------------------------------------------------
    # return [x for x in cisla if x%3 == 0 or x%5 == 0]

print(funkce2([7, 12, 35, 15, 45, 16, 18]))