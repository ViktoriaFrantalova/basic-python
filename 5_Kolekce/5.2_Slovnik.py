# Na vstupu získáte název barev a jejich počítačovou reprezentaci na přeskáčku. Vaším cílem je vytvořit slovník, který bude jako klíč obsahovat název barvy a jako hodnotu její reprezentaci. Vypište celý slovník

# Sample Input:

# červená #FF0000 modrá #0000FF zelená #008000 žlutá #FFFF00

# Sample Output:

#  {'červená': '#FF0000', 'modrá': '#0000FF', 'zelená': '#008000', 'žlutá': '#FFFF00'}

vstup = input().split( )
print(vstup) # ['červená', '#FF0000', 'modrá', '#0000FF', 'zelená', '#008000', 'žlutá', '#FFFF00']

dlzka = len(vstup) # 8

for farba in range(0, dlzka, 2): # kluc
    print(str(vstup[farba]))

for kod in range(1, dlzka, 2): # hodnota/ ak by bola intiger 
    hodnota = str(vstup[kod])
    print(hodnota)
    
zipStr = zip(vstup, hodnota)

vystup = dict(zipStr)
print(vystup)

#----------------------------------------------------------------
vstup = input().split( )
print(vstup) # ['červená', '#FF0000', 'modrá', '#0000FF', 'zelená', '#008000', 'žlutá', '#FFFF00']

dlzka = len(vstup) # 8

for i in range(0, dlzka):
    print(vstup[i], end=', ')
slovnik = dict(vstup)
print(slovnik)
#-------------------------------
# fungujuci

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
