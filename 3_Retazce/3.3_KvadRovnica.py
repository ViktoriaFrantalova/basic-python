# Tak a teďka napište znovu kód, který bude řešit kořeny kvadratické rovnice, ale proměnné a, b, c získejte ze standardního vstupu a výsledek vypište na standardní výstup. Čísla oddělujte mezerou.

vstup = input()
a, b, c = vstup.split()
D = float(b)**2 - 4*float(a)*float(c)
x1 = (-float(b) + D**0.5)/(2*float(a))
x2 = (-float(b) - D**0.5)/(2*float(a))
print(float(x1), float(x2))

# vstupne hodnoty napr. 1.0 -5.0 6.0
# vystup: 3.0 2.0