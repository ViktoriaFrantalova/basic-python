# KOSTKY

# Na vstupu získáte přirozené číslo. Najděte všechny způsoby, jak lze toto číslo získat při hodu dvěma hracími kostkami.

# Výsledek vypište jako seznam dvojic. Dvojice vypisujte ve tvaru (menší, větší) a seřaďte je podle prvního čísla. Pokud zadané číslo nelze získat při hodu dvěma kostkami, vraťte prostě prázdný seznam.

# Sample Input:

# 8

# Sample Output:

# [(2, 6), (3, 5), (4, 4)]

vstup = input()
vystup = ''
index = 0
for i in range(1, 7):
    for j in range(1, 7):
        if(i + j == int(vstup) and i <= j):
            if(index == 0):
                index += 1
                vystup = '(' + str(i) + ', ' + str(j) + ')'
            else:
                vystup += ', (' + str(i) + ', ' + str(j) + ')'
if(vystup != ''):
    print('[' + vystup + ']')