# Půlení
# Na vstupu získáte přirozené číslo. Zjistěte kolik krát po sobě lze toto číslo dělit dvěma (např. 40 --> 20 --> 10 --> 5, odpověď je 3krát)

# Sample Input 1:
# 40

# Sample Output 1:
# 3

# Sample Input 2:
# 7

# Sample Output 2:
# 0

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