# Je to číslo?

# Na vstupu získate řetězec, zjistěte jestli je to desetinné číslo. Pokud ano, vypište True; pokud ne, vypište False.

# Sample Input 1:
# -8.3

# Sample Output 1:
# True

# Sample Input 2:
# abc

# Sample Output 2:
# False

try:
    float(str(input()))
    print(True)
except ValueError:
    print(False)