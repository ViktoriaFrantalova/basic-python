# DOKUMENTACIA ZAKLADY PYTHONU

## 1. SYNTAX
# Komentare
* ak iba jeden riadok => #
* na viac riadkov => """..."""

```py
napeti = 5  # V s t u p n i n a p e t i [ V ]
def pocitej_odpor(napeti, proud): 
""" 
vypocet podla Ohmovho zakona [ V ] 
"""
odpor = napeti / proud     
return odpor 
``` 
# Premenne
* nesmie zacinat cislom a nesmie byt zhodna s klucovym slovom

```python
roky, polomer_kruhu, x1, x2, y...
```
* hodnotu priradam pomocou `=`
```python
a = 22
b = 10
```
# Dynamicke typovanie
* Python typuje hodnoty a premenne nemaju typ:
Zajladne typy: 
  - noneType - `None`
  - boolean - `True/False`
  - cele cisla - `integer (i)`
  - desatine/realne cisla - `float (f)`
  - komplexne cisla/komplexna zlozka j - `complex, 1+2j`
  - retazce - `str`
  - kolekcie - `list`, `dict`, `set`

```python
x = 22
type(x) # vypise sa int
```

# Funkce
* `type` 
```python
type(True) # vypise sa bool ako boolean
```
* `print`
```python
print("Hello") # vypise sa Hello
```
* `abs`
```python
abs(-5) # vypise sa 5, ako absolutna hodnota
```

* patria sem aj knihovni - `modules` => subor konstant, premennych a dalsich funkcii
`Moduly` - nacitam pomocou `import`

```python
import math
math.pi # vypise sa mi 3.14159... 

math.sqrt(2) # vypise sa odmocnina = 1.14142...

math.log(100) # prirodzeny logaritmus...

math.log10(100) # desiatkovy logaritmus...

math.sin(90) # sinus...

math.radians(90) # 1.5707963267948966

math.degrees(2 * math.PI) # 360.0
```

# Pretypovanie

```python
type(10) # vypise sa int

float(10) # vypise sa 10.0

type(float(10)) # vypise sa float

str(10) # vypise sa "10"

type(str(10)) # vypise sa str

```

# Bloky
* za pomoci dvojbodky a odsadzovania textu 
```python
def block1():
    a = 2 
    b = 3  
    def block2():
        c = 4
def block3():
    d = 4
```
* ak su zle odsadenia vyskoci error hlaska `IndentationError` 

# Matematicke operacie a operatory 
* klasicke operatory: +, -, *, /
```python
2 + 3 # vypise sa 5
```

* operator `modulo` => celociselne delenie: %, vracia zbytok
```python
10 % 3 # vypise sa zbytok 1
```

* mocniny a odmocniny
```python
2 ** 8 # vypise sa 256

16 ** 0.5 # vypise sa 4.0
```
* poradie matematickych funkcii je ako v matematiken

* porovnavacie operatory: <, >, =, ==, !=, <=, >=
```python
x = 5   # do premennej x priradi hodnotu 5! 
x == 5  # je x rovne 5
```
* logicke operatory: and, or, not

## 2. RETAZCE, VSTUPY A VYSTUPY

# Znak `(character)`
- je prvok konkretnej znakovej sady

# Retazce `(string)`
- postupnost znakovej
- zapis pomocou ',(tiez ked su uvodzovky) " alebo aj pri viacriadkovych retazcoch ''', """ 

```python
'Hello'
"Hello"
'''Hello'''
"""Hello"""

retezec = """dlouhy retezec
pres hodne radku"""
print(retezec) # dlouhy retezec pres hodne radku

print("I'm sorry.") # I'm sorry.
```
# Vypis retazcov funkcii `print`
- v normalnom aj interaktivnom mode, uvodzovky sa nevypisuju

```python
retazec = 'moj string'
print(retazec) # vypise sa: moj string
```
- iba v ineteraktivnom mode s uvodzovkami ak: 
```python
retazec = 'moj string'
retazec # vypise sa: 'moj string'
```
# Specialne znaky a escapovanie
- zapisujeme pomocou spatneho lomitka `\`
- Naj:
  - `\n` novy riadok 
  - `\t` tabulator
  - `\'` apostrof
  - `\"` uvodzovky
  - `\\` spatne lomitko

# Operzcie s retcami
- funkcia `len` - zisti dlzku retazca
```python
len('ahoj') # 4
len('Dobry den. \n') # 11
```
- operator `+` -> spojovanie retazca
```python
'dvě' + ' ' + 'slova' # 'dvě slova'
a = 2
b = 'slova'
str(a) + ' ' + b # '2 slova'
```
- operator `*` 
```python
'ha' * 5 # 'hahahahaha'
```
- volanie znakovej -> pomocou [] a indexu
- zaporne indexi sprava od -1  
```python
retezec = 'Hello World'
retezec[0] # 'H'
retezec[1] # 'e'
retezec[-1] # 'd'
retezec[-2] # 'l'
```
- podretazec -> zapisujem [od:do]
```python
retezec = 'Hello World'
retezec[2:5] # 'llo'
retezec[-4:] # 'orld'
retezec[:4] # 'Hell'
retezec[:] # 'Hello World'
```
- preskakovanie znaku [od:do:krok]
- vieme vynechat od, do alebo obe
- obrateny retazec - krok = -1
```python
retezec = '0123456789'
retezec[1:8:2] # '1357'

retezec[::3] # '0369'

retezec[::-1] # '9876543210'
```
# Retazec nemozno upravovat!
```python
retezec = 'Hello World'
retezec[6] = 'X' # error

retezec = retezec[:6] + 'X' + retezec[7:]
retezec # 'Hello Xorld'
```
- hladanie podretazcov `(substrings)`-> operatory in a not in testuju ci je/nie je ihla v kope sena
```python
'123' in 'ABCDefgh1234' # True
'456' in 'ABCDefgh1234' # False
'456' not in 'ABCDefgh1234' # True
'ABCDefgh1234' in '123' # False
```
- METODY: 
  * metoda `count()`- pocitam pocet
```python
retezec = 'Nesnese se se sestrou.'
retezec.count('se') # 4

'se'.count(retezec) # 0   
```
  * metoda `find()`- hladam index
```python
retezec = 'Nesnese se se sestrou.'
retezec.find('se') # 5 
```
  * metoda `startswith()`- hlada iba na zaciatku
  * metoda `endswith()`- hlada iba na konci
```python
retezec = 'Nesnese se se sestrou.'
retezec.startswith('se') # False

retezec.startswith('Nes') # True

retezec.endswith('.') # True
```
  * metoda `replace()`- nahradi stary podretazec za novy
    * treti parameter nastavi max pocet nahradeni
```python
'kormorán'.replace('or', 'ol') # 'kolmolán'

'kormorán'.replace('or', 'ol', 1) # 'kolmorán'
```
  * metoda `split()`-rozdeli retazec podla zadaneho separatoru
    * pokial nie je separator nastaveny beru sa defaultne zhluky bielych znakov(medzera, \t, \n)
```python
retezec = 'dvě slova \t tři celá slova'
retezec.split() # ['dvě', 'slova', 'tři', 'celá', 'slova']

retezec.split(' ') # ['dvě', '', 'slova', '\t', 'tři', 'celá', 'slova']
```
- odstranenie bielych znakov na okrajoch
  - metoda `strip()` - odstranenie z oboch koncov retazca
  - metoda `lstrip()` - odstranenie z lava (left-strip)
  - metoda `rstrip()` - odstranenie z prava (right-strip)

- zmena velkosti pisma 
  - metoda `upper()` - velke pismena
  - metoda `lower()` - male pismena
  - metoda `swapcase()` - zmena velkosti, male na velke a naopak
  - metoda `capitalize()` - prve pismeno velke v prvom slove
  - metoda `title()` - prve pismeno velke v kazdom slove
```python
retezec = 'ABCD efgh Ijkl'
retezec.upper() # 'ABCD EFGH IJKL'

retezec.lower() # 'abcd efgh ijkl'

retezec.swapcase() # 'abcd EFGH iJKL'

retezec.capitalize() # 'Abcd efgh ijkl'

retezec.title() # 'Abcd Efgh Ijkl'
```
# Logicke operacie 
- `isalpha()` - obs iba pismena
- `isdigit()` - obs iba cislice
- `isalnum()` - obs iba pismena a cisla
```python
'ABCDefgh1234'.isalnum() # True

'ABCD efgh 1234'.isalnum() # False
```
- `isspace()`- obs iba biele znaky
```python
' \t\n\r'.isspace() # True

'a \t\n\r'.isspace() # False
```
- `isupper()`, `islower()`-su vsetky psmena velke/male
```python
'Mám 5 jablíček.'.islower() # False

'mám 5 jablíček.'.islower() # True

'A Je To Tady'.istitle() # True
```
# Formatovanie retazca
1. metoda `format()` - mame sablonu do ktorej umiestnujeme znacku `{}`, kt sa nahradia hodnotamy y parametru funkcie
```python
sablona = 'Jmenuji se {} a je mi {} let.'
sablona.format('Anička', 5) # 'Jmenuji se Anička a je mi 5 let.'
```
   - znacky mozem indexovation a aj pomenovat
```python
sablona = 'Jmenuji se {}, je mi {} let, líbí se mi {}.'
sablona.format('Anička', 5, 'Prasátko Peppa')
# 'Jmenuji se Anička, je mi 5 let, líbí se mi Prasátko Peppa.'

sablona = 'Jmenuji se {2}, je mi {1} let, líbí se mi {0}.'
sablona.format('Anička', 5, 'Prasátko Peppa')
# 'Jmenuji se Prasátko Peppa, je mi 5 let, líbí se mi Anička.'

sablona = 'Jmenuji se {2}, je mi {0} let, líbí se mi {1}.'
sablona.format('Anička', 5, 'Prasátko Peppa')
# 'Jmenuji se Prasátko Peppa, je mi Anička let, líbí se mi 5.'

sablona = 'Jmenuji se {jmeno}, je mi {vek} let, líbí se mi {co}.'
sablona.format(vek=5, co='Prasátko Peppa', jmeno='Anička')
# 'Jmenuji se Anička, je mi 5 let, líbí se mi Prasátko Peppa.'
```
TYPY:
- vo znacke za dvojbodkov definujeme:
  - zarovnanie `{:<}`, `{:>}` alebo `{:^}`
  - dlzku `{:100}`
  - pocet desatinych miest `{:.2}`
  - typ1/format: `{:s}` retazec, `{:n}` cislo, `{:f}` realne cislo, `{:e}` vedecky format cisla
- zadane poradie je nutne dodrzat
```python
'{}'.format(1000.2) # '1000.2'

'{:>20.2e}'.format(1000.2) # '     1.00e+03'

'{x:^20.2E}'.format(x=1000.2) # '   1.00E+03   '
```
2. `f-string` - funguje podobne ako `format` ale znacky musia byt pomenovane
- hodnoty sa beru priamo z premennych v prostredi
```python
jmeno = 'Anička'
vek = 5
co = 'Prasátko Peppa'

f'Jmenuji se {jmeno}, je mi {vek:.2f} let, líbí se mi {co:^25}.'
# 'Jmenuji se Anička, je mi 5.00 let, líbí se mi      Prasátko Peppa     .'
```
# VSTUP (input) a VYSTUP (output)
- funkcia `input` - sluzi na predanie info. do beziaceho programu
  - uzivatelovi vypise hlasku, vysledok je retazec, kt. zadal uzivatel
```python
jmeno = input('Jak se jmenuješ? ')
vek = input('Kolik ti je let? ')
co = input('Co se ti líbí? ')
print(f'Jmenuješ se {jmeno}, je ti {vek} let, líbí se ti {co}.')

#Jak se jmenuješ? Honza
#Kolik ti je let? 7
#Co se ti líbí? Pokémoni
#Jmenuješ se Honza, je ti 7 let, líbí se ti Pokémoni.
```
- funkcia `output` teda `print` - sluzi na predanie info. von y beziaceho programu
  - vsetky parametre premeni na retazec a vypise ich
```python
print('ahoj', 5, True) # ahoj 5 True
```
# Specialne parametre funkcie `print()`: 
- `sep`(default je ' ')
```python
print(1, 2, 3) # 1 2 3

print(1, 2, 3, sep=', ') # 1, 2, 3

print(1, 2, 3, sep='\t') # 1     2     3

print(1, 2, 3, sep='') # 123
```
- `end`(default je '\n')
```python
print(1, 2, 3) # 1 2 3
print(4, 5, 6) # 4 5 6

print(1, 2, 3, end=';')
print(4, 5, 6)
# 1 2 3;4 5 6

print(1, 2, 3, sep=',', end=' ---> ')
print(4, 5, 6, sep='|', end='.')
# 1,2,3 ---> 4|5|6.
```
# Reprezentacia znakov v pocitaci
- kazdy znak je v znakovej sade reprezentovany svojim ordinalnym cislom
- funkcia `ord` zistuje ordinalne cislo znaku
- opakom je funkcia `chr`, ktora vracia znak pre zadane ordinalne cislo
```python
ord('A') # 65

ord('č') # 269

chr(97) # 'a'

chr(367) # 'ů'
```
- escapovanie pomocou ordinalnych cisel
  - `\x??` kde ?? je ord. cislo znaku v 16 sustave
  - `\u????` kde ???? je ord. cislo znaku 16 sustave
  - `\U????????` kde ???????? je ord. cislo znaku v 16 sustave
  - `\N{name}` kde name je nazov Unicode znaku 
```python
print('\x41 \u0041 \U00000041 \xE1 \N{pound sign}')
# A A A á £
```
## 3.PODMYNKY A CYKLY

# Logicke operatory
- `and` - "a" (logicky sucin)
- `or`  - "alebo" (logicky sucet)
- `not` - negacia
```python
'abc'.startswith('a') and 9 > 1 # True

not False # True
```
- operator `and` vracia lavu stranu vyrazu, pokial je nepravdiva, inak vracia pravu cast vyrazu
- opertator `or` vracia lavu stranu vyrazu, pokial je pravdiva, inak vracia pravu cast vyrazu
```python
None or 1 # 1

0 and True # False
10 and True # True
```

- in/ not in - je/nie je sucasti 
- is/ is not - testovanie identity objektu
```python
'abc' not in 'abcdef' # False

5 == 5.0 # True

5 is 5.0 # False
```
# poradie operacii
1. Matematicke: **, *, /, +, -
2. Porovnavacie: <, >, <=, >=, ==, !=, is is not, in , not in
3. not 
4. and
5. or   
```python
9 + 3 > 11 and 5 != 6 or not True # True
```
# Bloky
- casti kodu, kt sa vykonavaju v konkretnych situaciach
- zacinaju na predchadzajucom riadku dvojbodkou `:`
- su odsadene urcitym poctom medzier/tabulatorov
- bloky mozu byt aj vnorene

```python
if 1 == 2:
  print('1 == 2') # Blok 1
  print('This is strange') # Blok 1
elif 1 > 2:
  print('1 > 2') # Blok 2
  print('This is even stranger') # Blok 2
while 1 > 2: # Blok 2
  print('It is strange indeed') # Blok 2, vnorený blok 3
  x = 5 # Blok 2, vnorený blok 3
  y = x + 2 # Blok 2, vnorený blok 3
  print('Blablabla') # Blok 2
else:
  pass # Blok 4
  print('This is the end') # This is the end
```
- odsadenie celeho bloku musi byt rovnake, inak cakajte `IndentationError`
- doporucene odsadenie su  medzery, VS Code - automaticky nahradzuje tabulator za 4 medzery

```python
if 1 == 2:
    print('Hmmm...')
      print('I am confused')
# File "<ipython-input-13-d8dc889750bf>", line 3
# print('I am confused')
# ^
# IndentationError: unexpected indent
```
- bloky nemozu byt prazdne
```python
if 1 == 2:
else:
# File "<ipython-input-15-c11bbeb9214a>", line 2
# else:
# ^
# IndentationError: expected an indented block
```
- ked chceme blok, v kt. sa nerobi nic, pouzije prikaz `pass`
```python
if 1 == 2:
    pass
else:
    pass
```

# Podmienky
- `if` 
```python
if podminka:
    udelej_neco
```
```python
x = 15
if x > 10:
    print(f'{x} je vacsie ako 10.') # 15 je vacsie ako 10
print('Koniec') # Koniec 

x = 3
if x > 10:
    print(f'{x} je vacsie ako 10.')
print('Koniec') # Koniec
```
- `if.. else`
```python
if podminka:
    udelej_neco
else:
    udelej_neco_jine
```
```python
x = 15
if x > 10:
    print(f'{x} je vacsie ako 10.') # 15 je vacsie ako 10
else:
    print(f'{x} je menšie alebo rovne 10.')
print('Koniec') # Koniec

x = 3
if x > 10:
    print(f'{x} je vacsie ako 10.')
else:
    print(f'{x} je menšie alebo rovne 10.') # 3 je menšie alebo rovne 10
print('Koniec') # Koniec
```
- `if... elif... else`
- moze byt aj viacej podmienok s `elif`
```python
if podminka1:
    udelej_neco_1
elif podminka2:
    udelej_neco_2
else:
    udelej_neco_jine
```
- vykona sa vzdyiba prvy blok v kt. je splnena podmianka
```python
x = 8
if x > 10:
    print(f'{x} je vacsie ako 10.')
elif x > 5:
    print(f'{x} je vacsie ako 5.') # 8 je vacsie ako 5
else:
    print(f'{x} je menšie alebo rovne 5.')
print('Koniec') # Koniec
```
# Cykly  
- cyklus `while` 
```python
while podminka:
    udelej_neco
```
- jedno prevedenie udelej_neco sa nazyva jedna iterace 
- treba davat pozor na zacyklenie
```python
slovo = 'ozvěna'
while len(slovo) > 0:
    print(slovo)
    slovo = slovo[1:]
print('Konec')
# ozvěna
# zvěna
# věna
# ěna
# na
# a
# Konec
```
# Iterovatelne objekty (iterables)
- objekty, kt. vieme prechadzat po prvkoch (iterovat)
- napr. 
  - retazce: 'Ahoj' ---> 'A', 'h', 'o', 'j'
  - zoznamy: 'Dobrý den všem'.split() ---> 'Dobrý', 'den', 'všem'
- nevieme iterovat: 5, True, 3.14, print ... 

- cyklus `for` 
- určeny na iterovanie
```python
for i in iterable:
    udelej_neco(i)
```
```python
for znak in 'abcd':
    print(znak + '!')
# a!
# b!
# c!
# d!

for slovo in 'Toto je hezká věta'.split():
    print(slovo, len(slovo))
# Toto 4
# je 2
# hezká 5
# věta 4
```
# Rozsah, funckia `range()`
- reprezentuje postupnost cisel
- iterovany objekt  
```python
for i in range(5):
    print(i)
# 0
# 1
# 2  
# 3 
# 4 
```
- `for` cyklus a `range()`
```python
for i in range(5):
    print(i, i * 'ha')
#0
#1 ha
#2 haha
#3 hahaha
#4 hahahaha
```
- tri sposoby volania funkcie `range()`
  - s jednim argumentom `end`

range(10) ---> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

  - s dvoma argumentami `start`, `end`

range(3, 10) ---> 3, 4, 5, 6, 7, 8, 9

  - s troma argumentami `start`, `end`, `step`
  
range(3, 10, 2) ---> 3, 5, 7, 9

- vsetky argumenty musia byt `int` !!!  
- `start` je zahrnuty v rozsahu ale `end` nie

```python
for i in range(-5, 0):
    print(i, end=' ') # -5 -4 -3 -2 -1

for i in range(10, 0, -1):
    print(i, end=' ') # 10 9 8 7 6 5 4 3 2 1

for i in range(0, -10, -1):
    print(i, end=' ') # 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 
```

# Riadenie behu cyku pomocou `break` a `continue` 
- `continue` ukonci vykonavanie aktualnej iteracie a spusti nasledjucu
- `break` ukonci vykonavanie celeho cyklu
  
```python
for i in range(6):
    if i % 2 == 1:
        continue
    print(i)
print('Konec')
# 0
# 2
# 4
# Konec
```
```python
for i in range(6):
    if i % 2 == 1:
        break
    print(i)
print('Konec')
# 0
# Konec
```
# Riadenie cyklu `for` pomocou `break` a `else` 
- pokial cyklus prebehol cely(neukoncil sa pomocou `break`), spusti sa blok `else`
```python
for prvek in iterable:
    delej_neco ...
    break
    ...
else:
    udelej_neco_dalsi
```
```python
for i in range(30, 35):
    print(i)
    if i % 11 == 0:
        print(f'Nalezen násobek jedenácti: {i}')
        break
else:
    print('Žádné číslo dělitelné 11 nenalezeno.')
# 30
# 31
# 32
# 33
# Nalezen násobek jedenácti: 33
```
## 4.Kolekce   
- objekty, kt. obs. strukturne viac honot, vsetky kolekce su iterovane objekty 
- zakladne kolekce: 
  - `list` (zoznam) - upravovatelny zoznam zoradenich hodnot, [1, 5, 1]
  - `tuple` (n-tice) - neupraveny subor zoradenich hodnot so specifickym vyznamom(nechceme menit), (1, 5, 1)
  - `set` (mnozina) - upravovatelny subor unikatnych hodnot, {1, 5}
  - `dict` (slovnik) - slovnik nezoradenych hodnot indexovanych pomocou kluca, {'x': 1, 'y': 5}
- dalsie typy kolekce:
  - `namedtuple`
  - `defaultdict`
  - `OrderedDict`
  - `Counter`
  - `frozenset`
  - `deque`
  - ...

# Zoznam `list`
- vytvorime ho pomocou:
  - [] z jednotlivych prvkov 
  - funkcii `list` y ineho iterovatelneho objektu

- vieme ho modifikovat naroydiel od retazcov teda: menit, pridavat, odoberat prvky
- je to najcastejsie pouzivany typ kolekce
- na poradi zalezi !!!
- pouzitie: 
  -  ked mame viac obdobnych objektov ako zoznam cisel, zoznam studentov
```python
seznam = [1, 2, 3, 4, 5]
seznam # [1, 2, 3, 4, 5]

seznam = []
seznam # []

pismena = list('hello')
pismena # ['h', 'e', 'l', 'l', 'o']

cisla = list(range(5))
cisla # [0, 1, 2, 3, 4]

[1, 2, 3] == [1, 2, 3] # True
[1, 2, 3] == [1, 3, 2] # False
```
- Indexovanie
```python
seznam = [1, 2, 3, 4, 5]
seznam[2] # 3

seznam[-1] # 5

seznam[1:4] # [2, 3, 4]

seznam[:-2] # [1, 2, 3]
```

# Operacie so zoznamami
- `len` - dlzka
- `in`, `not in` - pritomnost prvku
- `count` - pocet vyskytu prvku
- `index` - prvi vyskyt prvku
```python
cisla = [1, 2, 5, 2]
len(cisla) # 4

5 in cisla # True

cisla.count(2) # 2 

cisla.index(2) # 1
```

- Zretazenie
```python
[1, 2] + [5, 2, 8] # [1, 2, 5, 2, 8]
```

- Opakovanie
```python
[1, 2] * 3 # [1, 2, 1, 2, 1, 2]
```

- Matematicke operacie `sum`, `min`, `max`
```python
cisla = [1, 2, 5, 2]
sum(cisla) # 10

min(cisla) # 1

max(cisla) # 5
```
- Logicke funkcie `all(vsetky prvky pravdive)` a `any(aspon 1 prvok pravdivy)`
```python
all([True, True, True, False]) # False
any([True, True, True, False]) # True
```

# Modifikacia zoznamu
```python
seznam # [1, 2, 3, 4, 5]

seznam[2] = 8
seznam # [1, 2, 8, 4, 5]
```
- Pridavanie prvkov
  - metoda `appender(prvok)` - prida novy prvok na koniec
  - metoda `insert(index, prvok)` - prida prvok na dany index
  - metoda `extend(iterable)` - prida na koniec zoznamu vsetky prvky z ineho iterovatelneho objektu
```python
seznam = [1, 2, 3]
seznam # [1, 2, 3]

seznam.append(4)
seznam # [1, 2, 3, 4]

seznam.insert(2, 10)
seznam # [1, 2, 10, 3, 4]

seznam.extend([1, 2, 3])
seznam # [1, 2, 10, 3, 4, 1, 2, 3]
```

- Odoberanie prvkov
  - metoda `pop()` - odobere posledny prvok a vrati ho ako vysledok
  - metoda `pop(i)` - odobere i-ty prvok a vrati ho ako vysledok
  - metoda `remove(prvok)`- odobere prvy vyskyt prvku
  - metoda `del` - odstrani prvok
```python
seznam # [1, 2, 10, 3, 4, 1, 2, 3]

x = seznam.pop() # Odstraň a vrať poslední prvek
print(seznam, x) # [1, 2, 10, 3, 4, 1, 2] 3

x = seznam.pop(2) # Odstraň a vrať druhý prvek
print(seznam, x) # [1, 2, 3, 4, 1, 2] 10

seznam # [1, 2, 3, 4, 1, 2]

seznam.remove(2) # Odstraň prvek 2
seznam # [1, 3, 4, 1, 2]
```

- Zmena smeru `reverse()`
```python
seznam # [1, 3, 4, 1, 2]

seznam.reverse()
seznam # [2, 1, 4, 3, 1]

del sesznam[2]
seznam # [1, 3, 1, 2]
```
- Usporiadanie
  - metoda `sort()` s volitelným parametrom `reverse`
```python
seznam = [1, 4, 2, -3, 5, 0]
seznam.sort()
seznam # [-3, 0, 1, 2, 4, 5]

seznam.sort(reverse=True)
seznam # [5, 4, 2, 1, 0, -3]

seznam = ['pes', 'kočka', 'slon']
seznam.sort()
seznam # ['kočka', 'pes', 'slon']

seznam.sort(key=len)
seznam # ['pes', 'slon', 'kočka']
```
# n-tice `tuple`
- vytvorime ho pomocou:
  - () z jednotlivych prvkov 
  - funkciou `tuple` z ineho iterovatelneho objektu
- nevieme modifikovat
- pouzivam ak maju prvky svoj specificky vyznam a nie je nutne modifikovat prvky => ulice, cislo, mesto
- indexovanie je rovnake ako u retazcov a zoznamov
```python
adresa = ('Vlhká', 5, 'Brno')
adresa # ('Vlhká', 5, 'Brno')

seznam # ['pes', 'slon', 'kočka']

ntice = tuple(seznam)
ntice # ('pes', 'slon', 'kočka')
```
- "Nultice" => empty tuple
```python
nultice = ()
nultice # ()
```

- "Jedince" => singleton
```python
jednice = (5,)
jednice # (5,)

cislo = (5)
cislo # 5
```

- Pozor na roydiel medzi "jedinci" a samotnym prvkom
```python
(5,) == 5 # False
```

# Operace s n-ticemi
- ako u zoznamu
```python
cisla = (1, 2, 3)
len(cisla) # 3

sum(cisla) # 6

cisla.count(8) # 0

cisla + cisla[::-1] # (1, 2, 3, 3, 2, 1)

cisla * 3 # (1, 2, 3, 1, 2, 3, 1, 2, 3)
```

# Mnozina `set`
- vytvorime ju pomocou:
  - {} y jednotlivych prvkov
  - funkcie `set` z ineho iterovatelneho objektu
- vieme ju modifikovat
```python
mnozina = {1, 2, 3}
mnozina # {1, 2, 3}

mnozina = set('hello')
mnozina # {'e', 'h', 'l', 'o'}
```
- kazdy prvok obsadeny najviac jeden-krat
```python
seznam = [1, 1, 2, 3, 3]
set(seznam) # {1, 2, 3}
```
- nevieme indexovat
```python
mnozina = {1, 2, 3}
mnozina[0]
# TypeError Traceback (most recent call last)
# <ipython-input-69-a0d66b3a8e7f> in <module>()
# 1 mnozina = {1, 2, 3}
# ----> 2 mnozina[0]
# TypeError: 'set' object does not support indexing
```
- Poradie nie je dane
```python
{1, 2, 3} == {3, 2, 1} # True
```
- prazdna mnozina sa yapisuje `set()`, pretoze {} je zarezervovane pre prazdny slovnik
```python
type(set()) # set  

type({}) # dict
```
# Operacie s mnozinamy
- `len` - pocet prvkov
- `in`, `not in` - pritomnost prvku (efektivnejsie ako pri zozname lebo nemusia sa kontrolovat vsetky prvky)
```python
A = {1, 2, 3}
len(A) # 3

2 in A # True
```
```python
A = {1, 2, 3}
B = {2, 4, 6}

A & B # Průnik A ∩ B
# {2}

A | B # Sjednocení A ∪ B
# {1, 2, 3, 4, 6}

A - B # Rozdíl množin A - B (prvky A kromě prvků B)
# {1, 3}

A <= B # A je podmnožinou B (A ⊆ B) 
# False

A < B # A je vlastní podmnožinou B (A ⊂ B)
# False
```

- Pridavanie prvkov
  - metoda `add()`
```python
A = set()
A.add(5)
A.add(6)
A # {5, 6}

A.add(5)
A # {5, 6}
```

- Odoberanie prvkov
  - metoda `discard(x)` - odoberie prvok `x` (ak tam x nie je nestane sa nic)
  - metoda `remove(x)` - odoberie prvok `x` (skonci chybou, pokial tam x nie je)
```python
A = set(range(5))
A # {0, 1, 2, 3, 4}

A.discard(2)
A # {0, 1, 3, 4}
```
  - metoda `pop()` - odoberie jeden lubovolny prvok a vrati ho ako vysledok
  - metoda `clear()` - odoberie vsetky prvky
```python
A # {0, 1, 3, 4}
x = A.pop()
x # 0 

A # {1, 3, 4}

A.clear()
A # set() 
```

# Slovnik `dict`
- vytvorime ho pomocou
  - {} y jednotlivych dvojic klucovych hodnot
  - funkcie `dict` z ineho iterovatelneho objektu
- slovnik vieme modifikovat
- kazdy kluc je obsiahnuty najviac jeden-kont
- indexujeme podla klucu (nie podla poradia)
```python
slovnik = {'klic1': 'hodnota1', 'klic2': 'hodnota2'}
slovnik # {'klic1': 'hodnota1', 'klic2': 'hodnota2'}

slovnik = {} # Prázdný slovník
slovnik # {}

seznam_dvojic = [('jack', 4098), ('sape', 4139), ('guido', 4127)]
slovnik = dict(seznam_dvojic)
slovnik # {'guido': 4127, 'jack': 4098, 'sape': 4139}
```
- Indexovanie pomocou kluca
```python
slovnik # {'guido': 4127, 'jack': 4098, 'sape': 4139}

slovnik['jack'] # 4098
slovnik['bob'] # error...
```
  - metoda `get()` je ako [], ale riesi i chybajuce kluce
```python
print(slovnik.get('guido')) # 4127

print(slovnik.get('bob')) # None

print(slovnik.get('bob', 'defaultni_hodnota')) # defaultni_hodnota
```
- Testovanie pritomnosti kluca
  - u slovnikov sa pomocou `in` dotazujeme na kluce/ nie na hodnoty
```python
slovnik = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
'a' in slovnik # True

1 in slovnik # False

1 in slovnik.values() # True
```
- Pridanie alebo uprava stavajucich hodnot
  - pokial kluc nie je v slovniku, prida sa a priradi sa mu hodnota
  - pokial kluc je vo slovniku, stara hodnota sa zahodi a prida sa nova
```python
slovnik # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

slovnik['bob'] = 1234
slovnik # {'a': 1, 'b': 2, 'bob': 1234, 'c': 3, 'd': 4} 

slovnik['guido'] = 666
slovnik # {'a': 1, 'b': 2, 'bob': 1234, 'c': 3, 'd': 4, 'guido': 666}
```
  - metoda `update` - prijma ako parameter dalsi slovnik, ktorym upravim stavajuci
```python
slovnik # {'a': 1, 'b': 2, 'bob': 1234, 'c': 3, 'd': 4, 'guido': 666}

slovnik.update({'guido': 1111, 'alice': 9876})
slovnik # {'a': 1, 'alice': 9876, 'b': 2, 'bob': 1234, 'c': 3, 'd': 4, 'guido': 1111}
```
  - metoda `pop` a `clear` ako u zoznamu

# Homegenne a heterogenne kolekce, kolekce v kolekci
- Homegenne kolekce - hodnoty rovnakeho typu [1, 2, 3]
- heterogenne kolekce - hodnotyzmiesaneho typu [1, 'ahoj', True]
- kolekce v kolekci
  - vynimka: Kluce v slovniku a prvky mnozin mozu byt iba nemodifikovatelne objekty
```python
[1, '2', 3.0, [4, 5], (6, 7)] 
# [1, '2', 3.0, [4, 5], (6, 7)]

{'a': [(1,),(1,2)], 'b': [(2,3),(1,)], 'c': [(9,),(1,)], 'd':[]}
# {'a': [(1,), (1, 2)], 'b': [(2, 3), (1,)], 'c': [(9,), (1,)], 'd': []}
```

# Rozbalovanie (unpacking)
- pomocou operatora `*`
- vytiahneme vsetky prvky z iterovatelneho objektu
```python
seznam = [1, 2, 3, 4]
print(seznam) # [1, 2, 3, 4]

rint(*seznam) # Stejné jako print(1, 2, 3, 4)
# 1 2 3 4

[0, seznam, 5, 6] # [0, [1, 2, 3, 4], 5, 6]

[0, *seznam, 5, 6] # Stejné jako [0, 1, 2, 3, 4, 5, 6]
# [0, 1, 2, 3, 4, 5, 6]
```
- pomocou viacej premennych na lavej strane priradenia
```python
seznam # [1, 2, 3, 4]

a, b, c, d = seznam
a # 1
b # 2

prvni, druhy, *zbytek, posledni = range(10)
prvni # 0
druhy # 1
zbytek # [2, 3, 4, 5, 6, 7, 8]
posledni # 9
```

# Prechadzanie kolekcie
- pomocou cyklu `for` 
```python
for prvek in {1, 2, 3, 2}:
print(prvek)
# 1
# 2
# 3
```
- cez kluc
```python
slovnik = {'guido': 4127, 'jack': 4098}
for jmeno in slovnik:
print(jmeno) 
# guido
# jack
```
- cez hodnotyzmiesaneho
```python
for telefon in slovnik.values():
print(telefon)
# 4127
# 4098
```
- cez kluce a hodnoty
```python
for jmeno, telefon in slovnik.items():
print(f'{jmeno}: {telefon}')
# guido: 4127
# jack: 4098
```
# Chytre prechadzanie kolekci
- funkcia `enumerate()` ocisluje prvky
```python
jmena = ['Bob', 'Alice', 'Cyril']
for i, jmeno in enumerate(jmena):
print(f'{i}. {jmeno}')
# 0. Bob
# 1. Alice
# 2. Cyril

for i, jmeno in enumerate(jmena, 1):
print(f'{i}. {jmeno}')
# 1. Bob
# 2. Alice
# 3. Cyril
```
- funkcia `reversed()` prechadza od konca
```python
for jmeno in reversed(jmena):
print(jmeno)
# Cyril
# Alice
# Bob
```
- funkcia `sorted()` vytvara novy zoradeni zoznam
```python
for jmeno in sorted(jmena):
print(jmeno)
# Alice
# Bob
# Cyril
```
- funckia `zip()` prechadza viac objektami na raz
```python
for jmeno, pismenko in zip(jmena, 'XYZW'):
print(jmeno, pismenko)
# Bob X
# Alice Y
# Cyril Z
```
POZOR !!! tieto funkcie nevytvaraju kolekce, iba iteratoe urceny k jednorazovemu prejdeni prvku
```python
iterator = reversed(jmena)
for jmeno in iterator:
print(jmeno)
# Cyril
# Alice
# Bob
```
# Generator vyrazu (generator expression)
- pomocou `for...in...` [if...] mozeme vztvarat a filtrovat kolekcie
```python
puvodni = [1, 2, 3, 4, 5, 6]
str(x) for x in puvodni]
# ['1', '2', '3', '4', '5', '6']

{i: i**2 for i in puvodni} 
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
```
- filtrujeme pridanim `if`
```python
{x for x in puvodni if x % 2 == 0}
# {2, 4, 6}
```
- typ vzslednej kolekce je dany typom zatvoriek: [zoznam], {mnozina} alebo slovnik
  - Vynimka: () vytvaraju iterator a nie n-tici
```python
(x for x in puvodni if x >= 3) # iterátor 
# <generator object <genexpr> at 0x7f887c3b09e8>

tuple(x for x in puvodni if x >= 3) # n-tice
# (3, 4, 5, 6)
```
- funkcia `join()` spojuje prvky pomocou separatoru, funguje ale iba na prvky typu `str`
```python
iterable = ['1', '2', '3']
' - '.join(iterable)
# '1 - 2 - 3'
```
# Vytvaranie noveho objektu vs modifikacie objektu
- vytvaranie noveho objektu:
```python
puvodni = 'Spam spam spam.'
novy = puvodni.replace('spam', 'ham')
print(puvodni) # Spam spam spam.
print(novy) # Spam ham ham.

puvodni = [1, 8, 5, 2]
novy = sorted(puvodni)
print(puvodni) # [1, 8, 5, 2]
print(novy) # [1, 2, 5, 8]
```
- modifikacia objektu:
```python
puvodni = [1, 8, 5, 2]
novy = puvodni.sort()
print(puvodni) # [1, 2, 5, 8]
print(novy) # None

puvodni = [1, 8, 5, 2]
novy = puvodni.append(0)
print(puvodni) # [1, 8, 5, 2, 0]
print(novy) # None
```
# Rovnake objekty vs ten isty objekt
  - Operatory: `==`, `!=` testuju, ci su dva objekty rovnake
  - Operatory: `is`, `is not` testuju, ci sa jedna o ten samy objekt
- rovnake objekty:
```python
a = [1, 2, 3]
b = [1, 2, 3]
a == b 
# True

a is b # False

a.append(4)
print(a, b) # [1, 2, 3, 4] [1, 2, 3]
```
- ten samy objekt:
```python
a = [1, 2, 3]
b = a
a == b
# True

a is b # True

a.append(4)
print(a, b) # [1, 2, 3, 4] [1, 2, 3, 4]
```
- vsetky modifikovatelne kolekce mozem duplikovat pomocou metody `copy()` - vytvorime tak novy objekt
```python
a = [6, 8, 3, 1]
b = a.copy()
b.sort()
print(a, b) # [6, 8, 3, 1] [1, 3, 6, 8]
```
