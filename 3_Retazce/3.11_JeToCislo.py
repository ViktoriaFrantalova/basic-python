# V tomto úkolu už víme, že pokaždé dostaneme číslo, ale nevíme jaké. Zjistěte jestli se jedná o liché nebo sudé číslo. Pro sudé číslo vypište 0 a pro liché vypište 1. (Podmínky jsme ještě nedělali, jde to bez nich.)

vstup_cislo = input()
test = (int(vstup_cislo)%2) or 0
print(test)

#-----------------------------------
print(int(input()) % 2)