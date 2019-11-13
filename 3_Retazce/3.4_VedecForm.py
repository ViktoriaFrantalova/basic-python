# Vstupní řetězec převeďte na číslo a vypište jako číslo ve vědeckém formátu.

# Sample Input:
# 40800000000.00000000000000

# Sample Output:
# 4.08E+10

vstup_str = input() 
x = float(vstup_str)
print('{:^20.2E}'.format(x))