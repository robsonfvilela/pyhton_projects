import random

print('='*60)
print(f'''
Este é um rolador de dados simples.

Para utilizá-lo, digite o nome do dado que deseja jogar:
d4
d6
d8
d10
d12
d20
''')

print('='*60)

dado = input('Dado: ')
    
if dado == 'd4':
    resultado = random.randint(1, 4)    
if dado == 'd6':
    resultado = random.randint(1, 6)
if dado == 'd8':
    resultado = random.randint(1, 8)
if dado == 'd10':
    resultado = random.randint(1, 10)
if dado == 'd12':
    resultado = random.randint(1, 12)
if dado == 'd20':
    resultado = random.randint(1, 20)

print(resultado)

