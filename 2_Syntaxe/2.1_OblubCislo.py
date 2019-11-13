# OBlibene cisla

# Alice, Bob a Cyril si chtějí vybrat společné oblíbené číslo.

# Alici se líbí dvouciferná čísla, která obsahují čtyřku.
# Bobovi se líbí čísla dělitelná třemi.
# Cyrilovi se líbi všechna čísla kromě násobků sedmi. 
# Zjistěte, jestli se zadané přirozené číslo n bude líbit všem třem.

# Sample Input 1:
# 45

# Sample Output 1:
# True

# Sample Input 2:
# 42

# Sample Output 2:
# False

# Sample Input 3:
# 12

# Sample Output 3:
# False

n = int(input())

libi_se_vsem = (n > 9 and n < 100 and '4' in str(n) and n % 3 == 0 and n % 7 != 0)

print(libi_se_vsem)