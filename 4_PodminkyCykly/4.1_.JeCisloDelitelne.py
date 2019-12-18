# Na vstupu získáme celé číslo od 0 do 100.
# 1. otestujte, jestli jsme dostali správné číslo (mezi 0 a 100)
# 2. otestujte, jestli je číslo dělitelné pěti, třemi nebo oběma čísly zároveň

# Na výstup vypište:
# - špatné číslo
# - číslo dělitelné 3 a 5
# - číslo dělitelné 3
# - číslo dělitelné 5
# - číslo nedělitelné 3 ani 5

# Sample Input:
# 4

# Sample Output:
# číslo nedělitelné 3 ani 5

vstup = int(input())

if vstup >= 0 and vstup <= 100:
    if vstup % 3 == 0 and vstup % 5 == 0:
        print("číslo dělitelné 3 a 5")
    elif vstup % 3 == 0:
        print("číslo dělitelné 3")
    elif vstup % 5 == 0:
        print("číslo dělitelné 5")
    elif vstup % 3 != 0 and vstup % 5 != 0:
        print("číslo nedělitelné 3 ani 5")
else: 
    print("špatné číslo")