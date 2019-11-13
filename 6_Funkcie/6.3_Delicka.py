# Delicka

# Napište funkci delicka, která bude přijímat parameter text a volitelný parameter separator (defaultní separátor = ';'). Funkce rozdělí text podle parametru separator, převede první dva prvky na reálná čísla a vrátí jejich podíl.

# Sample Input 1:
# delicka('1;2;haha')

# Sample Output 1:
# 0.5

# Sample Input 2:
# delicka('3 2 ... ... ...', separator=' ')

# Sample Output 2:
# 1.5

def delicka(text: str, separator: str = ';') -> float:
    prvy, druhy, *_ = text.split(separator)
    return float(prvy) / float(druhy)

print(input())




