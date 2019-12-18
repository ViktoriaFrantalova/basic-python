"""
Úloha:
Pomocí souboru cofactors.json najděte všechny sloučeniny, které jsou kofaktorem 
nějaké hydrolázy. (V klasifikaci enzymů EC tvoří hydrolázy třídu 3, 
hledáme tedy všechny záznamy, které mají v "EC" uvedené aspoň jedno číslo 
začínající trojkou.)
Hint: Pro přehledné zobrazení souboru cofactor.json ve VSCode klikněte 
pravým tlačítkem na text a zvolte Format document.
Zdroj dat: https://www.ebi.ac.uk/pdbe/api/doc/compounds.html, část Cofactors

Vzorový výstup:  
Phosphopantetheine
Nicotinamide-adenine dinucleotide
Adenosylcobalamin
Flavin adenine dinucleotide
Tetrahydrofolic acid
Coenzyme A
Flavin Mononucleotide
Menaquinone
Heme
Glutathione
S-adenosylmethionine
Thiamine diphosphate
Pyridoxal 5'-phosphate
"""


import json

with open('cofactors.json') as f:
    cofactors = json.load(f)

selected = []

for compound, data in cofactors.items():
    enzymes = data[0].get('EC', [])
    if any(enzyme.startswith('3.') for enzyme in enzymes):
        selected.append(compound)

print(*selected, sep='\n')
