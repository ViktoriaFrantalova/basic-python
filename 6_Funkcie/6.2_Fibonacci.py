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

#--------------------------------------------------
# from typing import List

# def fibonacci(n: int) -> List[int]:
#     if n == 0:
#         return []
#     elif n == 1:
#         return [1]
#     else:
#         vysledek = [1, 1]
#         while len(vysledek) < n:
#             nove_cislo = vysledek[-2] + vysledek[-1]
#             vysledek.append(nove_cislo)
#         return vysledek

# print(eval(input()))  # Neměňte! Do not change!


# # Alternativní řešení:
# from typing import List

# def fibonacci(n: int) -> List[int]:
#     if n == 0:
#         return []
#     elif n == 1:
#         return [1]
#     else:
#         vysledek = [1, 1]
#         for i in range(n - 2):
#             vysledek.append(sum(vysledek[-2:]))
#         return vysledek

# print(eval(input()))  # Neměňte! Do not change!

