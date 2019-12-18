# 4. (16 bodů) Napište definici funkce funkce4, která vezme jako parametr řetězec obsahující jménaa příjmení osob oddělené čárkami (před a za čárkou může být libovolný počet mezer, mezi jménema příjmením je jedna nebo více mezer, každá osoba má pouze jedno jméno a jedno příjmení).Funkce přeformátuje jména osob do formátu “Příjmení, Jméno”, jednotlivé osoby oddělí středníkem a mezerou (viz doctest). Návratovou hodnotou je takto přeformátovaný řetězec.

from typing import Dict, List, Tuple
from pprint import pprint

def funkce4(osoby: str) -> str:
      """Přeformátuj jména.
      >>> funkce4('Cyril   Novák ,    Alice Černá,Bob  Marley')
      'Novák, Cyril; Černá, Alice; Marley, Bob'
      """
      osoby = osoby.split(',')
      seznam_preformatovanych = []
      for osoba in osoby:
            jmeno, prijmeni = osoba.split()  # split() bez argumentu automaticky sdružuje bílé znaky, tj. není třeba je odstraňovat například pomocí strip()
            seznam_preformatovanych.append(f'{prijmeni}, {jmeno}')
      vysledek = '; '.join(seznam_preformatovanych)
      return vysledek


print(funkce4('Cyril   Novák ,    Alice Černá,Bob  Marley'))

