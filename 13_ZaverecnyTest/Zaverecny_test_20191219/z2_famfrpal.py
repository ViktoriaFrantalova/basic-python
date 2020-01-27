## koment ucitela: Parsovanie záznamov je OK, ale tá druhá časť počíta niečo úplne iné, než by mala.

from typing import List, Dict
from pprint import pprint


PRIKLAD = '''Gryffindor:Hufflepuff:200:120  Ravenclaw:Slytherin:180:210 
Hufflepuff:Ravenclaw:80:240   Gryffindor:Slytherin:200:310 
Ravenclaw:Gryffindor:80:180   Slytherin:Hufflepuff:50:160'''


def celkove_skore(zaznamy: str) -> Dict[str, int]:
    """
    >>> pprint(celkove_skore(PRIKLAD))
    {'Gryffindor': 580, 'Hufflepuff': 360, 'Ravenclaw': 500, 'Slytherin': 570}
    >>> pprint(celkove_skore(''))
    {}
    """
    
    vysledok = {}
    casti = zaznamy.split()
    for i in range(len(casti)):
        zapas = casti[i].split(':')

        vysledok[zapas[0]] = zapas[2]
        vysledok[zapas[1]] = zapas[3]

        if(list(vysledok.keys())[0] == zapas[0]):
            vysledok[zapas[0]] = int(vysledok[zapas[0]]) + int(zapas[2])

        if(list(vysledok.keys())[1] == zapas[1]):
            vysledok[zapas[0]] = int(vysledok[zapas[0]]) + int(zapas[2])

    return vysledok


pprint(celkove_skore('''Gryffindor:Hufflepuff:200:120  Ravenclaw:Slytherin:180:210 
Hufflepuff:Ravenclaw:80:240   Gryffindor:Slytherin:200:310 
Ravenclaw:Gryffindor:80:180   Slytherin:Hufflepuff:50:160'''))