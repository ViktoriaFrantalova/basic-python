# Filter 2

# Napište definici funkce muj_filter, která přijímá seznam čísel (mohou být int i float). Funkce bude vracet trojici obsahující minimum, maximum a seznam se zbylými čísly. 

# Sample Input:

# muj_filter([15, 10, 5, 20, 25.2])

# Sample Output:

# (5, 25.2, [15, 10, 20])

def muj_filter(cisla: list) -> tuple:
    min_cislo = cisla[0]
    max_cislo  = cisla[0]
    zvysok = []
    for cislo in range(0, len(cisla)):
        if (cisla[cislo] > max_cislo):
            max_cislo = cisla[cislo]
        if (cisla[cislo] < min_cislo):
            min_cislo = cisla[cislo]
    for cislo in range(0, len(cisla)):
        if (cisla[cislo] != max_cislo and cisla[cislo] != min_cislo):
            zvysok.append(cisla[cislo])
    return (min_cislo, max_cislo, zvysok)
    
print(muj_filter([15, 10, 5, 20, 25.2]))  