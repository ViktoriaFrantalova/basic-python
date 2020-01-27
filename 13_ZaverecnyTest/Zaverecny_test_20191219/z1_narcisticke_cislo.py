## koment ucitela: Na konci stačilo “return sucet == int(n)”

def je_narcisticke(n: int) -> bool:
    """
    >>> je_narcisticke(5)
    True
    >>> je_narcisticke(10)
    False
    >>> je_narcisticke(42)
    False
    >>> je_narcisticke(153)
    True
    >>> je_narcisticke(8028)
    True
    """
    sucet = 0
    pocet_cifier = len(str(n))
    n = str(n)
    for cifra in n:
      medzi_sucet = int(cifra) ** int(pocet_cifier)
      sucet = sucet + int(medzi_sucet)
    if int(sucet) == int(n):
      return True
    else:
      return False

print(je_narcisticke(153))