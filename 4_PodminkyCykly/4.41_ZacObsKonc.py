# Začíná, končí nebo obsahuje?
# Na vstupu získáte dva řetezce. Otestujte jestli první řetězec začíná, končí nebo pouze obsahuje druhý řetězec. 

# Možné výstupy:

# "{}" začíná a končí "{}"
# "{}" začíná "{}"
# "{}" končí "{}"
# "{}" obsahuje "{}"
# "{}" neobsahuje "{}"
# Místo {} doplňte první a druhý řetězec.

# Sample Input:
# abcabc abc

# Sample Output:
# "abcabc" začíná a končí "abc"

kupka_slamy, jehla = input().split(' ')
realita = jehla in kupka_slamy
if realita == True:
    if kupka_slamy.startswith(jehla) and kupka_slamy.endswith(jehla) == True:
        print(f'"{kupka_slamy}" začíná a končí "{jehla}"')
    elif kupka_slamy.startswith(jehla) == True:
        print(f'"{kupka_slamy}" začíná "{jehla}"')
    elif kupka_slamy.endswith(jehla) == True:
        print(f'"{kupka_slamy}" končí "{jehla}"')
    elif realita:
        print(f'"{kupka_slamy}" obsahuje "{jehla}"')
else:
    print(f'"{kupka_slamy}" neobsahuje "{jehla}"')

