# Kalkulacka

# Na vstupu získate dvě desetinná čísla oddělená matematickým operátorem. Proveďte výpočet a vypište výsledek zaokrouhlený na 2 desetinná místa.

# Možné operace:

# sčítání +
# odečítání -
# násobení *
# dělení /
# Pokud bude zadaný nepovolený operátor, vypište na výstupu None.

# Sample Input:
# 1 + 2

# Sample Output:
# 3.00

cislo_1, znamienko, cislo_2 = input().split(' ')
if znamienko == '+':
    riesenie = float(cislo_1) + float(cislo_2)
    print('{:.2f}'.format(riesenie))
elif znamienko == '-':
    riesenie = float(cislo_1) - float(cislo_2)
    print('{:.2f}'.format(riesenie))
elif znamienko == '/':
    riesenie = float(cislo_1) / float(cislo_2)
    print('{:.2f}'.format(riesenie))
elif znamienko == '*':
    riesenie = float(cislo_1) * float(cislo_2)
    print('{:.2f}'.format(riesenie))
else:
    print('None')