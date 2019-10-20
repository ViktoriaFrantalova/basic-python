# Půlení
# Na vstupu získáte přirozené číslo. Zjistěte kolik krát po sobě lze toto číslo dělit dvěma (např. 40 --> 20 --> 10 --> 5, odpověď je 3krát)

# napr
# input - 40
# output - 3

# input - 7
# output - 0

vstup = input()
pocet_deleni = 0
while True:
    vysledok = vstup
    if (int(vysledok) % 2 != 0):
        break
    vysledok = int(vstup) / 2
    pocet_deleni = pocet_deleni + 1
print(pocet_deleni)