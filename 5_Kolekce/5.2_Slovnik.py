# Na vstupu získáte název barev a jejich počítačovou reprezentaci na přeskáčku. Vaším cílem je vytvořit slovník, který bude jako klíč obsahovat název barvy a jako hodnotu její reprezentaci. Vypište celý slovník

# Sample Input:
# červená #FF0000 modrá #0000FF zelená #008000 žlutá #FFFF00

# Sample Output:
#  {'červená': '#FF0000', 'modrá': '#0000FF', 'zelená': '#008000', 'žlutá': '#FFFF00'}

vstup = input().split( )
vystup = set()
farba = ''
for i in range(len(vstup)):
    if(i % 2 == 0):
        farba += "'" + str(vstup[i]) + "': "
    else:
        if(i == len(vstup) - 1):
            farba += "'" + str(vstup[i]) + "'"
        else:
            farba += "'" + str(vstup[i]) + "', "

print('{' + farba + '}')

# # Alternativní řešení:
# casti = input().split()
# barvy = casti[0::2]
# kody = casti[1::2]
# slovnik = {}
# for barva, kod in zip(barvy, kody):
#     slovnik[barva] = kod
# print(slovnik)

# # Alternativní řešení: 
# casti = input().split()
# barvy = casti[0::2]
# kody = casti[1::2]
# slovnik = {barva: kod for barva, kod in zip(barvy, kody)}
# print(slovnik)

# # Alternativní řešení 2:
# casti = input().split()
# slovnik = {}
# for i in range(0, len(casti), 2):  # iterujeme ob 1
#     barva = casti[i]
#     kod = casti[i+1]
#     slovnik[barva] = kod
# print(slovnik)
