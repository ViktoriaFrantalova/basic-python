# Vstupní řetězec převeďte na číslo a vypište jako číslo ve vědeckém formátu.

vstup_str = input() # 40800000000.00000000000000
x = float(vstup_str)
print('{:^20.2E}'.format(x)) # 4.08E+10