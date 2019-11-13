# Najdi palindrom

# Napište definici funkce najdi_palindrom, která bere parametry veta a n. Funkce ve větě najde palindrom délky n a vrátí ho jako návratovou hodnotu. Pokud se ve větě žádný takový palindrom nenachází, funkce vyhodí chybu typu LookupError.  (Funkce bude ignorovat velikost písmen a mezery.)

# Sample Input 1:
# 'Petr jede v kajaku', 5

# Sample Output 1:
# 'kajak'

# Sample Input 2:
# 'Kuna nanuk nemá ráda', 9

# Sample Output 2:
# 'kunananuk'

# Sample Input 3:
# 'Miluji Python', 3

# Sample Output 3:
# LookupError

def najdi_palindrom(veta: str, n: int) -> str:
    pole = veta.split()
    slovo = ''
    vysledok = False
    for index in range(0, len(pole)):
        slovo = slovo + pole[index]
    slovo2 = ''
    for i in range(0, len(slovo)):
        slovo2 = slovo[(i+1-n):(i+1)]
        if(len(slovo2) == n):
            if (slovo2.lower() == slovo2[::-1].lower()):
                vysledok = slovo2.lower()
    if(vysledok == False):
        raise LookupError()
    return vysledok

# vstup = input()
# veta, n = vstup.split(', ')
print(najdi_palindrom('Petr jede v kajaku', 5))