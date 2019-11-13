# Řadové číslovky - pokračování

# Napište definici funkce order_numbers, která jako argument přijme seznam přirozených čísel, seřadí je od největšího po nejmenší, a vypíše je na terminál spolu s jejich pořadím. V řešení můžete volat funkci ordinal (bude fungovat tak, jak byla zadána v předchozí úloze).

from typing import List

def order_numbers(numbers: List[int]) -> None:
	"""
	>>> order_numbers([10, 5, 30, 18, 2, 25])
	1st is 30
	2nd is 25
	3rd is 18
	4th is 10
	5th is 5
	6th is 2
	"""
	zoradenie = sorted(numbers,reverse=True) # od najvacsieho po najmensie
	for index in range(1,len(zoradenie)):
		print(index)
		if index < 20:
			if index == 1:
				pripona = 'st'
			elif index == 2:
				pripona = 'nd'
			elif index == 3:
				pripona = 'rd'
			else:
				pripona = 'th'  
		else:   #pripona for > 20
			desiatky = str(index)
			desiatky = desiatky[-2]
			jednotky = str(index)
			jednotky = jednotky[-1]
			if desiatky == "1":
				pripona = "th"
			else:
				if jednotky == "1": 
					pripona = 'st'
				elif jednotky == "2":
					pripona = 'nd'
				elif jednotky == "3":
					pripona = 'rd'
				else:
					pripona = 'th'
		moj_index = index
		moja_pripona = pripona
	return (f'{moj_index}{moja_pripona}')

print(order_numbers([10, 5, 30, 18, 2, 25]))