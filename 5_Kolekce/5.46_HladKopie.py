# Hledame kopie

# Na vstupu získáte několik slov, z nichž dvě jsou stejná. Vypište, o které slovo se jedná a na kterých dvou pozicích se nachází (pozice počítáme od nuly).

# Hint: Jde to i bez použití funkcí jako find nebo index. Stačí využít vhodný typ kolekce.

# Sample Input:
# košík bouda kokos olovo mango kokos užovka karate

# Sample Output:
# kokos 2 5

vstup = input()
pole = vstup.split( )
for i in range(len(pole)):
    if(str(pole[i]) in str(pole[i + 1:len(pole)]) or str(pole[i]) in str(pole[0: i])):
        hladane_slovo = pole[i]
    if(str(pole[i]) in str(pole[i + 1:len(pole)])):
        pozicia_prve_slovo = i
    if(str(pole[i]) in str(pole[0: i])):
        pozicia_druho_slovo = i
print(hladane_slovo, pozicia_prve_slovo, pozicia_druho_slovo)