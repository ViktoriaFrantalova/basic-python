# SLOVNIK
#Na vstupu získáte klice#hodnoty, vytvořte slovník a vyberte hodnotu pro klíč utery.

# Sample Input:

# pondeli#rizek utery#smazak streda#halusky ctvrtek#gulas patek#smazak

# Sample Output:

# smazak

vstup = input().split(' ')
for i in vstup:
    if('utery' in i):
        vstup = i.split('#')
        for j in vstup:
            if('utery' not in j):
                print(j)

