# Caesarova šifra

# Na vstupu získate číslo a zprávu. Tato zpráva je posunutá o počet znaků podle zadaného čísla. Zprávu dekódujte a vypište. Mezery mezi znaky ignorujte.

# Nápověda:
# Funkce print s parametrem end nezalamuje výstup na nové řádky. Použijte funce chr a ord.

# Vyzkoušejte také: 
# -3#Jrf rf rnxz

# Sample Input:
# 5#Rfrf rjqj rfxt

# Sample Output:
# Mama mele maso

posun, zprava = input().split("#")
for i in zprava:
    if ord(i) == 32: # lebo (space)
        sifrovanie = int(ord(i))
    else:
        sifrovanie = int(ord(i) - int(posun))
    print(chr(sifrovanie), end = '')
