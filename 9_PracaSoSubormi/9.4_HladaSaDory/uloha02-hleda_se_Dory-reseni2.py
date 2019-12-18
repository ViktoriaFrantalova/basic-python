"""
Úloha:
Vytvořte program, který projde všechny soubory v adresáři CSFD a vypíše 
na výstup názvy všech souborů obsahujúcich v textu slovo Dory.

Vzorový výstup:  
Hleda_se_Dory.txt
Hleda_se_Nemo.txt

Bonus:
Modifikujte program tak, aby prohledával celý adresářový strom. 
Tj. aby našel například také soubor CSFD/Pohadky/Animovane/Hleda_se_Nemo.txt.
"""

import os


def soubor_obsahuje(nazev_souboru: str, hledany_text: str, encoding='utf8') -> bool:
    """
    Zjisti, jestli soubor nazev_souboru ve svém textu obsahuje hledany_text. 
    Vrať False, pokud soubor nelze otevřít nebo se jedná o adresář.
    """
    try:
        with open(nazev_souboru, encoding=encoding) as f:
            text = f.read()
        return hledany_text in text
    except (FileNotFoundError, PermissionError, IsADirectoryError):
        return False


hledane_slovo = 'Dory'

os.chdir('CSFD')
soubory = os.listdir()

for soubor in soubory:
    if soubor_obsahuje(soubor, hledane_slovo):
        print(soubor)
