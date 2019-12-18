# 5. (16 bodů) Napište definici funkce funkce5, která vezme jako parametr řetězec obsahující celá čísla oddělená mezerami. Funkce vrátí:
# • řetězec '+', pokud je víc kladných než záporných čísel
# • řetězec '-', pokud je víc záporných než kladných čísel
# • řetězec '?', pokud je stejný počet kladných a záporných čísel.

from typing import Dict, List, Tuple

def funkce5(cisla: str) -> str:
    """Zjisti, jestli řetězec obsahuje víc kladných nebo záporných čísel.
    >>> funkce5('5 10 -3 8 -1 0')
    '+'
    >>> funkce5('-555')
    '-'
    >>> funkce5('100 -8')
    '?'
    """
    seznam = [int(s) for s in cisla.split()]
    kladnych = zapornych = 0
    for x in seznam:
        if x > 0:
            kladnych += 1
        elif x < 0:
            zapornych += 1
    if kladnych > zapornych:
        return '+'
    elif kladnych < zapornych:
        return '-'
    else:
        return '?'
    #vzorove riesenie
    # seznam = [int(s) for s in cisla.split()]
    # kladnych = sum(1 for x in seznam if x > 0)
    # zapornych = sum(1 for x in seznam if x < 0)
    # if kladnych > zapornych:
    #     return '+'
    # elif kladnych < zapornych:
    #     return '-'
    # else:
    #     return '?'

print(funkce5('5 10 -3 8 -1 0'))