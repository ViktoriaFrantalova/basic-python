# Emívulm uktápzop

# Napište funkci veta_pozpatku, která bere jako argument větu a vrátí tuto větu s všemi slovy pozpátku. K tomu si napište pomocnou funkci slovo_pozpatku, která bere pouze jedno slovo a to vrátí pozpátku. (Velikost písmen a interpunkci neřešte.)

# Sample Input:
# veta_pozpatku('toto je tajná zpráva')

# Sample Output:
# otot ej ánjat avárpz

def veta_pozpatku(veta: str) -> str:
    pole = veta.split()
    dlzka_pola = len(pole)
    vysledok = ''
    for index in range(0, dlzka_pola):
        vysledok = slovo_pozpatku(pole[dlzka_pola - index -1]) + ' ' + vysledok
    return vysledok

def slovo_pozpatku(slovo: str) -> str:
    return ''.join(reversed(slovo))

print(eval(input()))