# V zadaném textu najděte první výskyt mezery a tři znaky, které za ní následují.

string = input() # Zítra bude krásné počasí.
medzera_index = string.find(' ')
print(medzera_index)
print(string[1+medzera_index:4+medzera_index])
# 5
# bud