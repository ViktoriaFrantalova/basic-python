"""
Úloha:
Alice háže kostkou 10x. Jaká je šance, že z těchto 10 hodů padnou aspoň 4 šestky?
Úlohu řešte pomocí simulace, tj. náhodně vygenerujte 10 hodů kostkou (modul random) 
a rozhodněte, jestli padly aspoň 4 šestky. Toto opakujte 10000 krát a spočítejte, 
jaké procento pokusů bylo úspěšné.
(Správný výsledek je kolem 7 %, samozřejmě to vždy vyjde trochu jinak.)

Bonus:
Bob háže kostkou 100x. Jaká je šance, že se mu v rámci těchto 100 hodů podaří hodit 
4 šestky PO SOBĚ?
(Správný výsledek je kolem 6 %).
"""

import random
import math


def simuluj_4x6(n_hodu: int) -> bool:
    """Simuluj n_hodu hodů kostkou a vrať True, pokud padly aspoň 4 šestky."""
    hody = [random.randint(1, 6) for i in range(n_hodu)]
    return hody.count(6) >= 4

def simuluj_4x6_po_sobe(n_hodu: int) -> bool:
    """Simuluj n_hodu hodů kostkou a vrať True, pokud padly aspoň 4 šestky po sobě."""
    hody = [random.randint(1, 6) for i in range(n_hodu)]
    hody_retezec = ''.join(str(x) for x in hody)
    return '6666' in hody_retezec


n_pokusu = 10000
uspesnych_Alice = 0
uspesnych_Bob = 0

for i in range(n_pokusu):
    if simuluj_4x6(10):
        uspesnych_Alice += 1

pravdepodobnost_Alice = uspesnych_Alice / n_pokusu

for i in range(n_pokusu):
    if simuluj_4x6_po_sobe(100):
        uspesnych_Bob += 1

pravdepodobnost_Bob = uspesnych_Bob / n_pokusu

print(f'Pravděpodobnost - Alice: {pravdepodobnost_Alice}')
print(f'Pravděpodobnost - Bob: {pravdepodobnost_Bob}')
