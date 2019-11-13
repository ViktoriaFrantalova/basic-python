# Bezpečný průměr

# Napište funkci prumer, která bere jako parametr seznam reálných čísel a vrací jejich průměr (pomocí klasického vzorce suma / počet).

# Zamyslete se nad tím, jaké problémy by mohly během výpočtu nastat, a napište funkci tak, aby neskončila chybou. Pokud průměr nelze spočítat, vraťte hodnotu math.nan (nan = not a number).

# Sample Input:
# [2, 7, 9]

# Sample Output:
# 6.000

import math
from typing import List

def prumer(cisla: List[float]) -> float:
    try:
        priemer = sum(cisla) / len(cisla)
        return priemer
    except (ZeroDivisionError, TypeError):
        return math.nan

cisla = input()
print(prumer(cisla))