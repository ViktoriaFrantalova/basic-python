# Filter

# Napište definici funkce nasobky3, která přijímá seznam celých čísel. Návratovou hodnotou funkce bude přefiltrovaný seznam čísel, které jsou dělitelné 3 beze zbytku.

# Řádek print(eval(input())) zabezpečí, že vaše funkce se bude volat přesně tak, jak je uvedeno na vzorovém vstupu. Nemusíte tedy načítat vstup ani vypisovat výstup, stačí naimplementovat funkci.

# Sample Input:

# nasobky3([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# Sample Output:

# [3, 6, 9, 12]

from typing import List

def nasobky3(cisla: List[int]) -> List[int]: 
    vysledok = []
    for i in range(0,len(cisla)):
        vstup = cisla[i]
        if(cisla[i] % 3 == 0):
            if(vstup == cisla[i]):
                vysledok.append(cisla[i])
    return vysledok
        
print(nasobky3([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))