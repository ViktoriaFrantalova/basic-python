# # 1. (16 bodů) Napište definici funkce funkce1, která vezme jako parametr seznam kladných reálných čísel – každé číslo představuje poloměr kruhu. Funkce vypíše na výstup poloměr a obsah každého kruhu v následujícím formátu:
#  Poloměr | Obsah
#  0.25 | 0.20
#  1.20 | 4.52
#  100.00 | 31415.93

# (Každý sloupec má šířku 8 znaků, mezi nimi je trojice znaků mezera-svislítko-mezera. Hodnoty se vypisují na 2 desetinná místa zarovnané doprava. Obsah kruhu S = πrr2.)

from typing import Dict, List, Tuple
from pprint import pprint

import math

def funkce1(polomery: List[float]) -> None:
    """Formátuj poloměr a obsah kruhů.
    >>> funkce1([100, 1.2, 0.25])
     Poloměr |    Obsah
      100.00 | 31415.93
        1.20 |     4.52
        0.25 |     0.20
    """
    #moje riesenie
    print(' Polomer |     Obsah')
    for cisla in range(0, len(polomery)):
        polomer = polomery[cisla]
        obsah = math.pi * polomer ** 2
        print(f'{polomer:>8.2f}'+ ' | ' + f' {obsah:>8.2f}')
    # vzorove riesenie
    # print(' Poloměr |    Obsah')
    # for r in polomery:
    #     S = math.pi * r**2
    #     print(f'{r:>8.2f} | {S:>8.2f}')
        
print(funkce1([100, 1.2, 0.25]))
