"""
Úloha:
Vytvořte program, který načte CSV soubor Brno_denni_teploty.csv.
Následně spočítá průměrnou teplotu pro každý měsíc v letech 1961-2017.
Výsledné průměrné hodnoty uloží do souboru Brno_mesicni_teploty.csv, a to 
tak, že každý řádek bude odpovídat jednomu roku a každý sloupec jednomu 
měsíci v roku. Vzorový výsledek najdete v Brno_mesicni_teploty-vzor.csv.
Zdroj dat: http://portal.chmi.cz/historicka-data/pocasi/denni-data

Bonus: 
Upravte program tak, aby přijímal název vstupního a výstupního souboru 
jako argumenty z příkazové řádky (hint: využijte modul argparse).
"""


import csv

with open('Brno_denni_teploty.csv') as f:
    for i in range(4):  # Ignorujeme hlavičku (první 4 řádky)
        f.readline()
    temperatures_by_years = {}
    for row in csv.reader(f):
        year = row[0]
        month = row[1]
        temperatures = [float(field) for field in row[2:] if field != '']
        average = sum(temperatures) / len(temperatures)
        if int(year) == 2017:
            print(f'{month}: {average:6.2f}')
        if year not in temperatures_by_years:
            temperatures_by_years[year] = []
        temperatures_by_years[year].append(average)

with open('Brno_mesicni_teploty.csv', 'w') as g:
    csv_writer = csv.writer(g)
    header = [''] + list(range(1, 13))
    csv_writer.writerow(header)
    for year, temperatures in temperatures_by_years.items():
        row = [year] + [f'{temp:.1f}' for temp in temperatures]
        csv_writer.writerow(row)
    