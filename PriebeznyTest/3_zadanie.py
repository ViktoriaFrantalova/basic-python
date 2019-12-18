# 3. (16 bodů) Sekvence DNA se skládá ze čtyř typů nukleových bazí (A, C, G, T). Relativní četnost
# báze vyjádřuje, jaká část sekvence je tvořena daným typem báze (počet výskytů báze / délka
# sekvence). Součet relativních četností je tedy vždy roven 1.
# Napište definici funkce funkce3, která vezme jako parametr sekvenci DNA a vrátí slovník s
# relativní četností nukleových bazí. (Poznámka: funkce pprint v doctestu vypisuje obsah slovníku
# seřazen podle klíčů, pořadí tedy nemusíte řešit. Hodnoty není potřeba nijak zaokrouhlovat.)
from typing import Dict, List, Tuple
from pprint import pprint

import math

def funkce3(sekvence: str) -> Dict[str, float]:
    """Spočítej relativní četnosti bazí v sekvenci DNA.
    >>> pprint(funkce3('ACGTTTTGAG'))
    {'A': 0.2, 'C': 0.1, 'G': 0.3, 'T': 0.4}
    >>> pprint(funkce3('AAA'))
    {'A': 1.0, 'C': 0.0, 'G': 0.0, 'T': 0.0}
    """
    delka = len(sekvence)
    relativni_cetnosti = {baze: sekvence.count(baze) / delka for baze in 'ATGC'}
    return relativni_cetnosti
    #-------------------------------------------------
    # cetnosti = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    # for baze in sekvence:
    #     cetnosti[baze] += 1
    # delka = len(sekvence)
    # for baze in cetnosti:
    #     cetnosti[baze] /= delka
    # return cetnosti

print(funkce3('ACGTTTTGAG'))