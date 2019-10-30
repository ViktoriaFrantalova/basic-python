# Řešíme kvadratickou rovnici pomocí funkce

# Napište definici funkce koreny, která přijímá tři číselné parametry a, b, c. Výstupem funkce budou kořeny kvadratické rovnice v n-tici. Počítejte s tím, že zadaná kvadratická rovnice může mít dva, jeden nebo žádný kořen.

# Řádek print(eval(input())) zabezpečí, že vaše funkce se bude volat přesně tak, jak je uvedeno na vzorovém vstupu. Nemusíte tedy načítat vstup ani vypisovat výstup, stačí naimplementovat funkci.

# Sample Input 1:

# koreny(1.0, -5.0, 6.0)
# Sample Output 1:

# (3.0, 2.0)

# Sample Input 2:

# koreny(1.0, -2.0, 1.0)
# Sample Output 2:

# (1.0,)

from typing import Tuple

def koreny(a: float, b: float, c: float) -> Tuple[float, float]:
    D = b**2 - 4*a*c
    if D > 0:
      x2 = (-b + D**0.5) / (2*a)
      x1 = (-b - D**0.5) / (2*a)
      return (x1, x2)
    elif D == 0:
      x = (-b) / 2*a
      return (x,)
    else:
      return ()

print(koreny(1.0, -2.0, 1.0)) 




