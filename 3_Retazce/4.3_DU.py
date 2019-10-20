# Na vstupu získate posloupnost znaků a jeden znak. V posloupnosti nahraďte první výskyt tohoto znaku za znak s obracenou velikostí (např. v za V nebo Z za z). Nápověda: funkce replace s parametrem count a funkce swapcase.

vstup = input() # AbCDabcd b
posledny_znak = vstup[-1]
vystup = vstup[::-1].replace(posledny_znak, '', 1).strip()[::-1]
vystup = vystup.replace(posledny_znak, posledny_znak.swapcase(), 1)
print(vystup) # ABCDabcd