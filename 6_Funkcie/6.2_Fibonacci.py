# Fibonacciho posloupnosti

# Napište funkci, která získá jako parametr počet prvků Fibonacciho posloupnosti a ty vrátí ve formě seznamu.

# Sample Input:
# fibonacci(6)

# Sample Output:
# [1, 1, 2, 3, 5, 8]

from typing import List
zoznam = []
def fibonacci(n: int) -> List[int]:
    vysledok = []
    a = 1
    b = 1
    for i in range(n):
        vysledok.append(b)
        scitanec = b + a
        b = a
        a = scitanec
    return vysledok

print(fibonacci(6))

