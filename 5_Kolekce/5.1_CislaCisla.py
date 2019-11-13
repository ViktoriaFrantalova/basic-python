# Na vstupu získate seznam čísel oddělených mezerou. Spočítejte a vypište minimum, maximum, průměr a medián. Vypište poslední číslo.

# Vyzkoušejte i tento vstup:
# 3 9 4 8 2 1

# Sample Input:
# 15 13 7 10 11

# Sample Output:
# Min: 7.00 Max: 15.00 Avg: 11.20 Med: 11.00
# Last number: 11

moj_zoznam = input().split()
dlzka = len(moj_zoznam) # pocet cisel v zozname
for prvok in range(0, dlzka):
    moj_zoznam[prvok] = int(moj_zoznam[prvok])
# iny zapis 1 2 3 4 8 9
# moj_zoznam = [int(x) for x in moj_zoznam]    
sortovany_zoznam = sorted(moj_zoznam, reverse=False) # [7, 10, 11, 13, 15]
maxi = max(moj_zoznam) # maximalne cislo
mini = min(moj_zoznam) # minimalne cislo
avg = (sum(moj_zoznam) / dlzka) # priemer
x = round(dlzka / 2) # zaokruhly
if dlzka % 2 != 0:
    med = sortovany_zoznam[x]
else:
    med = ((int(sortovany_zoznam[x - 1]) + int(sortovany_zoznam[x])) / 2)
    
posledne_cislo = moj_zoznam.pop() # posledne cislo

print('Min:', '{:.2f}'.format(mini), 'Max:', '{:.2f}'.format(maxi), 'Avg:', '{:.2f}'.format(avg), 'Med:','{:.2f}'.format(med))
print('Last number:', posledne_cislo)