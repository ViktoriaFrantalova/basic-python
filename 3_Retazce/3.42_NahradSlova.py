# V zadaném textu najděte všechny výskyty slova "je" a nahraďte je za slovo "bude". Nezapomeňte opravený text vypsat.

# Sample Input:
# Honza je doktor.

# Sample Output:
# Honza bude doktor.

string = input()
nahrada = string.replace('je', 'bude')
print(nahrada)