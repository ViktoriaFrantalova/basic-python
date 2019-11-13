# Záplava čísel
# Na vstupu získáte řetězec obsahující pouze číslice. Vypište na výstup řetězec, který bude obsahovat každou číslici ze vstupu tolik krát, kolik je hodnota číslice (tj. dvě dvojky, pět pětek atd...).

# Sample Input:
# 25104

# Sample Output:
# 225555514444

vstup = input()
for i in vstup:
    print(int(i) * i, end= '')