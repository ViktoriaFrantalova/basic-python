# Nejčastěji se opakující číslo

# Napište definici funkce nejcastejsi, která přijímá seznam čísel a vrací nejčastěji se opakující číslo v tomto seznamu.

# Pokud bude seznam prázdný, vraťte None. Pokud bude víc různých čísel se stejným, maximálním počtem výskytů, vraťte jedno z nich - je jedno které.

# Sample Input:
# [1, 2, 3, 3, 4, 4, 1, 2, 5, 3, 2, 1, 2]

# Sample Output:
# 2

from typing import List

def nejcastejsi(cisla: List[int]) -> int:
    sort_cisla = sorted(cisla)
    if (len(sort_cisla) == 0):
        return None
    pole = []
    vysledok= []
    for cislo in sort_cisla:
        if cislo not in pole:
            pole.append(cislo)
            
    pocet = 0
    posledny_pocet = 0
    pole_pocet = []
    vysledok = 0
    for cisloI in range(0, len(pole)):
        for cisloJ in range(0, len(sort_cisla)):
            if (pole[cisloI] == sort_cisla[cisloJ]):
                pocet = pocet + 1
                if(pocet > posledny_pocet):
                    posledny_pocet = pocet
                    vysledok = pole[cisloI]
            else:
                pocet = 0
    return vysledok
                    
print(nejcastejsi([1, 2, 3, 3, 4, 4, 1, 2, 5, 3, 2, 1, 2]))