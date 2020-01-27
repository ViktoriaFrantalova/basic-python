## koment ucitela: Dobrý začiatok, do csv.reader trebalo nastaviť delimiter=‘ ’

import csv

def main() -> None:
    with open('cities.csv', encoding='utf8') as csv_subor:
        print(csv_subor.read())
        reader = csv.reader(csv_subor)
        for line in reader:
            print(line)
        

vzdialenost = 


if __name__ == '__main__':
    main()
