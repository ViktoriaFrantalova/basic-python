# Hlada sa pozicia navacsie cisla

# Na vstupu získate jednotlivá čísla oddělená mezerou, vaším úkolem je nalézt pozici (index) největšího čísla. Pokud bude více největších čísel, vraťte pozici prvního.

# Vyzkoušejte také:
# 1 1 1 1 1
# nebo
# 2 3 4 5 1

# Sample Input:
# 1 2 3 4 5 10 7 8

# Sample Output:
# 5


vstup = input().split( )
dlzka = (len(vstup))

for i in range(0, dlzka):
    vstup[i] = int(vstup[i])
    
maxi = max(vstup) # maximalne cislo
if vstup.count(int(maxi)) > 1:
    print(vstup.index(int(maxi)))
else:
    print(vstup.index(int(maxi)))

# # Alternativní řešení:
# retezce = input().split()
# cisla = [int(r) for r in retezce]
# maximum = max(cisla)
# index_maxima = cisla.index(maximum)
# print(index_maxima)
