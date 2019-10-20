# Ze vstupu získejte dvě čísla a spočítejte mocninu. První číslo (float) je základ, druhé číslo (int) je exponent.

# zakladexponent

# Úlohu řešte pomocí cyklu, bez použití operátoru ** nebo funkce pow.

vstup = input() # 2.0 3
zaklad, exponent = vstup. split(' ')
n = 1

for i in range(1, int(exponent) + 1):
    n = n * float(zaklad)
print(float(n)) # 8.0
