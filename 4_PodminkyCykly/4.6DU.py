# Půlení
# Na vstupu získáte přirozené číslo. Zjistěte kolik krát po sobě lze toto číslo dělit dvěma (např. 40 --> 20 --> 10 --> 5, odpověď je 3krát)

# napr
# input - 40
# output - 3

# input - 7
# output - 0

vstup = int(input())
pocet_deleni = 0
cislo = 0
while True:
    if(vstup % 2 == 0):
        pocet_deleni = pocet_deleni + 1
        vstup = vstup / 2
    else:
        break
print(pocet_deleni)