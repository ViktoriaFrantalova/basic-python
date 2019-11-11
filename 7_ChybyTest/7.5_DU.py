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
  veta = veta.replace(" ","") # bez medzier
  veta = veta.lower() # iba male pismena
  naopak = veta[::-1] # string naopak
  return naopak

  i = n-1
  for i in range(0, len(naopak)):
      veta_nova = naopak[i]
      return veta_nova

vstup = input()
veta, n = vstup.split(', ')
print(najdi_palindrom(vstup))