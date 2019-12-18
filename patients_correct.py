"""
Opravte chyby v tomto programu.

Zadání: 
Spočítej a vypiš body mass index (BMI) všech pacientů ze seznamu patients.

Očekávaný výstup:
Patient's BMI is: 21.6
Patient's BMI is: 22.2
Patient's BMI is: 51.9
"""

patients = [(70, 1.8), (80, 1.9), (150, 1.7)]  # Hmotnost a výška jednotlivých pacientů

def calculate_bmi(weight: float, height: float) -> float:
    """Spočítej BMI pacienta o hmotnosti weight a výšce height.
    >>> f'{calculate_bmi(70, 1.8):.1f}'
    '21.6'
    """
    return weight / (height ** 2)

for patient in patients:
    weight, height = patient  # Chceme informace o konkrétním pacientovi, ne o nultém pacientovi.
    bmi = calculate_bmi(weight, height)  # První argument je hmotnost, druhý výška, ne naopak.
    print(f"Patient's BMI is: {bmi:.1f}")  # Při formátování pomocí f-stringu musí být před úvozovkami f.

