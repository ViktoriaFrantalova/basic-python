# Seznam čísel

# Napište definici funkce cisla, která přijímá řetězec. Řetězec rozdělte podle ";" a prvky, které nelzou převést na číslo, ignorujte. Návratovou hodnotou funkce bude seznam čísel (float).

# Vaše funkce bude volána takto:

# retezec = intput()
# print(cisla(retezec))

# Sample Input:
# 8;1;2.2;_;5.3;9.8

# Sample Output:
# [8.0, 1.0, 2.2, 5.3, 9.8]

from typing import List

def cisla(retezec: str) -> List[float]:
    retezec = retezec.split(';')
    zoznam = []
    for i in range(0,len(retezec)):
        try:
            vstup = float(retezec[i])
            zoznam.append(vstup)
        except ValueError:
            i = i + 1
    return zoznam

retezec = input()
print(cisla(retezec))
