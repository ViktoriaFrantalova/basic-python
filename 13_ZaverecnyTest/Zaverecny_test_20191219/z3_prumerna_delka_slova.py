## koment ucitela: Chýba tam odstránenie ‘.’ a ‘,’ a vyhodenie výnimky, keď počet slov je 0.

import math

def prumerna_delka_slova(text: str) -> float:
    """
    >>> round(prumerna_delka_slova('první ukázka'), ndigits=3)
    5.5
    >>> round(prumerna_delka_slova('Dobrý den.'), ndigits=3)
    4.0
    >>> round(prumerna_delka_slova('Orel klínoocasý je druh jestřábovitého ptáka, který se vyskytuje v Austrálii a Tasmánii, na jihu Nové Guineje a blízkých ostrovech. Patří mezi největší druhy orlů vůbec a je to největší dravý pták Austrálie.'), ndigits=3)
    5.182
    >>> round(prumerna_delka_slova('Skutek ... utek'), ndigits=3)
    5.0
    >>> round(prumerna_delka_slova('...'), ndigits=3)
    Traceback (most recent call last):
    ValueError
    """
    sucet = 0
    zoznam_dlzok = []
    vstupne_pole = text.split()
    pocet_slov = len(vstupne_pole)
    try:
        for slovo in vstupne_pole:
          dlzka_slova = len(slovo)
          sucet = sucet + int(dlzka_slova)
          zoznam_dlzok.append(dlzka_slova)
        priemerna_dlzka_slova = float(sucet) / float(pocet_slov)
        return priemerna_dlzka_slova
    except ValueError:
        print(ValueError)

print(prumerna_delka_slova('Dobrý den.'))