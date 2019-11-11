# Převrácená hodnota

# Zadaný vstup se pokuste převést na číslo N, a vypočítejte pro něj převrácenou hodnotu 1/N . Pokud se to nepovede, vypište None.

# Sample Input 1:
# 10

# Sample Output 1:
# 0.1

# Sample Input 2:
# 0

# Sample Output 2:
# None

try:
    N = int(input())
    n = 1 / N
    print(n)
except (ZeroDivisionError, ValueError):
    print(None)