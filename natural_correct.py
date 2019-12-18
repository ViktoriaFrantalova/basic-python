"""
Opravte chyby v tomto programu.

Zadání: 
Ze seznamu retezce vyber pouze řetězce reprezentující přirozená čísla a tato čísla vypiš na výstup.

Očekávaný výstup:
[1, 56]
"""

from typing import List

retezce = ['1', '-5', '56', '0', 'xxx']

def je_prirozene_cislo(retezec: str) -> bool:
    """Zjisti jestli řetězec reprezentuje přirozené číslo.
    >>> je_prirozene_cislo('666')
    True
    >>> je_prirozene_cislo('-10')
    False
    >>> je_prirozene_cislo('xyz')
    False
    """
    if retezec.isdigit() and int(retezec) > 0:  # V Pythonu se "a zároveň" píše vždy jako "and". Operátor & má úplne jiný význam!
        return True  # Odsazení
    else:
        return False  # Odsazení
    
def pouze_prirozena_cisla(retezce: List[str]) -> List[int]:
    """Vyber řetězce reprezentující přirozená čísla a vrať seznam těchto čísel.
    >>> pouze_prirozena_cisla(['1', '-5', '56', '0', 'xxx'])
    [1, 56]
    """
    cisla = []
    for prvky in retezce:
        if je_prirozene_cislo(prvky):
            cisla.append(int(prvky))  # Chceme celá čísla (int), ne reálná (float).
    return cisla

print(pouze_prirozena_cisla(retezce))