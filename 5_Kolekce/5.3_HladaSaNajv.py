# Hlada sa navacsie cislo
# Na vstupu získate jednotlivá čísla oddělená mezerou, vaším úkolem je nalézt pozici (index) největšího čísla. Pokud bude více největších čísel, vraťte pozici prvního.

vstup = input().split( )
dlzka = (len(vstup))

for i in range(0, dlzka):
    vstup[i] = int(vstup[i])
    
maxi = max(vstup) # maximalne cislo
if vstup.count(int(maxi)) > 1:
    print(vstup.index(int(maxi)))
else:
    print(vstup.index(int(maxi)))
