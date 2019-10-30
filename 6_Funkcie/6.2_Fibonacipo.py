# Fibonacciho posloupnosti

# Napište funkci, která získá jako parametr počet prvků Fibonacciho posloupnosti a ty vrátí ve formě seznamu.

# Sample Input:

# fibonacci(6)

# Sample Output:

# [1, 1, 2, 3, 5, 8]

from typing import List
zoznam = []
def fibonacci(n: int) -> List[int]:
    if n < 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        for i in range(n-2):
            nove_cislo = zoznam[-2] + zoznam[-1]
            zoznam.append(nove_cislo)
        return zoznam

print(fibonacci(6))

