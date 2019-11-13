# Oko

# Ve hře Oko (Blackjack) je cílem získat co největší počet bodů, ne však víc než 21. Přitom karty 2 až 10 mají při svou vlastní hodnotu; karty J, Q, K (spodek, královna, král) mají hodnotu 10; eso (A) má hodnotu 11.

# Např. mám-li na ruce karty 3, 5, K, 2, pak mám 3+5+10+2 = 20 bodů. Mám-li na ruce karty 6, J, A, pak mám 0 bodů, protože 6+10+11 = 27, což je víc než 21.

# Na vstupu získáte posloupnost karet oddělených čárkami. Spočítejte, za kolik bodů se tyto karty počítají, a výsledek vypište na výstup.

# input: 2, 3, 5, K
# output: 20

# input: 6, J, A
# output: 0

vstup = input().split(', ')
vysledok = 0
for i in vstup:
    if(str(i) == 'J' or str(i) == 'Q' or str(i) == 'K'):
        i = 10
    if(str(i) == 'A'):
        i = 11
    vysledok += int(i)
    
if(vysledok <= 21):
    print(vysledok)
else:
    print(0)
