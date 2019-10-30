# Nejdelší a nejkratší slovo

# V zadaném vstupu najděte najdelší a nejkratší slovo

# Sample Input:

# pes kočka holub slepice sokol anaconda slon liška

# Sample Output:

# anaconda
# pes

vstup = input().split(' ')
index = 0
for i in vstup:
    if(index == 0):
        hladane_najdlhsie_slovo = len(i)
        hladane_najkratsie_slovo = len(i)
        index += 1
    if (hladane_najdlhsie_slovo <= len(i)):
        hladane_najdlhsie_slovo = len(i)
        najdlhsie_slovo = i
    if(hladane_najkratsie_slovo >= len(i)):
        hladane_najkratsie_slovo = len(i)
        najkratsie_slovo = i

print(najdlhsie_slovo + '\n' + najkratsie_slovo)