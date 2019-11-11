# Tajná zpráva

# Napište definici funkce desifruj, která přijme zakódovanou větu (vše bude malými písmeny bez diakritiky a interpunkce). Vaším úkolem je přečíst jednotlivá slova pozpátku a vrátit celou dekódovanou zprávu.

def desifruj(tajna_zprava: str) -> str:
  """
  >>> desifruj('ibil es im anaj')
  'libi se mi jana'
  >>> desifruj('medjup recev tip')
  'pujdem vecer pit'
  """
  nova_sprava = []
  moja_sprava = tajna_zprava.split()
  for slovo in moja_sprava:
    nove_slovo = slovo[::-1]
    nova_sprava.append(nove_slovo)
  vysledok = ''
  for slovo  in nova_sprava:
    vysledok = vysledok + ' ' +  slovo
  return vysledok

print(desifruj('ibil es im anaj'))