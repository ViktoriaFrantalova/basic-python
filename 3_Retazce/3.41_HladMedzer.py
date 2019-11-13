# V zadaném textu najděte první výskyt mezery a tři znaky, které za ní následují.

# Sample Input:
# Zítra bude krásné počasí.

# Sample Output:
# 5
# bud

string = input()
medzera_index = string.find(' ')
print(medzera_index)
print(string[1+medzera_index:4+medzera_index])
