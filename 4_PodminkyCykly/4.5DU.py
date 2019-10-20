# Záplava čísel
# Na vstupu získáte řetězec obsahující pouze číslice. Vypište na výstup řetězec, který bude obsahovat každou číslici ze vstupu tolik krát, kolik je hodnota číslice (tj. dvě dvojky, pět pětek atd...).

# napr
# input - 25104 

# output - 225555514444

vstup = input()
for i in vstup:
    print(int(i) * i, end= '')