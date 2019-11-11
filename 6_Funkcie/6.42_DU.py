# Nejkratší a nejdelší

# Napište definici funkce kratke_dlouhe, která přijmá řetězec. Výstupem funkce bude n-tice obsahující dvě slova, nejkratší slovo a nejdelší slovo. Vstup nebude obsahovat interpunkci.

# Sample Input:
# kratke_dlouhe('Moje nejoblíbenější hračka byl plyšový medvídek Pú')

# Sample Output:
# ('Pú', 'nejoblíbenější')

from typing import Tuple

def kratke_dlouhe(retezec: str) -> Tuple[str, str]:
    pole_vstupov = retezec.split( )
    dlhe_slovo = pole_vstupov[0]
    kratke_slovo = pole_vstupov[0]
    dlzka_vstupneho_pola = 0
    for i in range(0, len(pole_vstupov)):
        dlzka_vstupneho_pola = len(pole_vstupov[i])
        if(dlzka_vstupneho_pola > len(dlhe_slovo)):
            dlhe_slovo = pole_vstupov[i]
        if(dlzka_vstupneho_pola < len(kratke_slovo)):
            kratke_slovo = pole_vstupov[i]
    return (kratke_slovo, dlhe_slovo)
    
print(kratke_dlouhe('Moje nejoblíbenější hračka byl plyšový medvídek Pú'))