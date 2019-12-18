"""
Opravte chyby v tomto programu.

Zadání: 
Načítej od uživatele požadovaný počet prvků Fibonacciho posloupnosti a ty vypiš na výstup.
"""

from typing import List

def fibonacci(n: int) -> List[int]:
    """Spočítej prvních n prvků Fibonacciho posloupnosti.
    >>> fibonacci(8)
    [1, 1, 2, 3, 5, 8, 13, 21]
    """
    x = []
    a = 0
    b = 1
    for i in range(n):  # Řídící proměnnou cyklu nesmí být a, protože by se na začátku každé iterace přepsala jeho hodnota.
        x.append(b)
        c = a + b
        a = b
        b = c
    return(x)  # Odsazení

def print_fibonacci() -> None:
    """Vypiš uživatelem zadaný počet prvků Fibonacciho posloupnosti."""
    n = input('Zadej požadovaný počet prvků Fibonacciho posloupnosti: ')  # Na velikosti písmen záleží. Proměnná N je jiná než n.
    n = int(n)  # Funkce input vrací řetězec. Před dalším použitím ho potřebujeme převést na celé číslo.
    print(fibonacci(n))

print_fibonacci()
