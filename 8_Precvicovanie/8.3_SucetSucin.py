# Součet a součin

# Napište definici funkce soucet_a_soucin, která jako argument dostane seznam čísel a vrátí jejich součet a součin.

# Dále doplňte kód, který ze vstupu načte řádek s reálnými čísly , zavolá funkci soucet_a_soucin a vypíše jejich součet a součin (formát viz Sample Output).

# Sample Input:
# 1.5 2.0 4.0

# Sample Output:
# Součet:    7.50
# Součin:   12.00

from typing import List, Tuple

def soucet_a_soucin(cisla: List[float]) -> Tuple[float, float]:
    """
    >>> soucet_a_soucin([1.5, 2.0, 4.0])
    (7.5, 12.0)
    >>> soucet_a_soucin([0.25, 10.5, 0.75, -2.0, 2.0])
    (11.5, -7.875)
    """
    pass  # tento řádek nahraďte řešením


# Sem doplňte kód pro načtení čísel a výpis výsledků