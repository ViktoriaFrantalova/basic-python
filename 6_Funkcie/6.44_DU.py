# Společná písmena

# Napište definici funkce spolecna_pismena, která přijímá seznam řetězců. Funkce vrátí seznam znaků, které se vyskytují v každém z těchto řetězců. Seznam bude seřazen podle abecedy. Pokud bude funkce volána na prázdném seznamu, vrátí prázdný seznam.

# Sample Input:

# spolecna_pismena(['mrkev', 'krkavec', 'krabice'])
# Sample Output:

# ['e', 'k', 'r']

from typing import List

def spolecna_pismena(retezce: List[str]) -> List[str]:
    if(len(retezce) == 0):
        return retezce
    najkratsi_vstup = retezce[0]
    for i in range(0, len(retezce)):
        if(len(najkratsi_vstup) < len(retezce[0])):
            najkratsi_vstup = retezce[0]                  
    retezce.remove(najkratsi_vstup)
    pole_bez_najkratsieho_vstupu = retezce

    pole_nerovnakych_znakov = []
    for i in range(0, len(pole_bez_najkratsieho_vstupu)):
        predosli_znak = najkratsi_vstup[0] 
        for j in range(0, len(najkratsi_vstup)):
            if (
                najkratsi_vstup[j] not in pole_bez_najkratsieho_vstupu[i] and
                najkratsi_vstup[j] not in pole_nerovnakych_znakov
            ):
                pole_nerovnakych_znakov.append(najkratsi_vstup[j])
    pole_rovnakych_znakov = []
    for i in range(0, len(najkratsi_vstup)):
        if(najkratsi_vstup[i] not in pole_nerovnakych_znakov):
            pole_rovnakych_znakov.append(najkratsi_vstup[i])
    vysledok = []
    for i in range(0, len(pole_rovnakych_znakov)):
        if (pole_rovnakych_znakov[i] not in vysledok):
            vysledok.append(pole_rovnakych_znakov[i])
    vysledok.sort()
    return vysledok
    
print(spolecna_pismena(['mrkev', 'krkavec', 'krabice']))