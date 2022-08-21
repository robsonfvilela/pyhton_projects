# Título: Rolador de Dados de RPG
# Versão: 02
# Data: 2022-08-19
# Changelog: Agora pode escolher quantos dados rolar. Adicionado d100.

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
d100

Em seguida, digite a quantidade de dados.
''')
print('='*60)

dado = input('Dado: ').upper()
quantidade = int(input('Quantidade: '))
sum=0

if dado == 'D4':
    for i in range(1,quantidade+1):
        resultado = random.randint(1,4)
        sum = sum+resultado
        print('Você rolou um D4 e obteve:', resultado)


if dado == 'd6':
    for i in range(1,quantidade+1):
        resultado = random.randint(1,6)
        sum = sum+resultado
        print('Você rolou um D6 e obteve:', resultado)


if dado == 'd8':
    for i in range(1,quantidade+1):
        resultado = random.randint(1,8)
        sum = sum+resultado
        print('Você rolou um D8 e obteve:', resultado)


if dado == 'd10':
    for i in range(1,quantidade+1):
        resultado = random.randint(1,10)
        sum = sum+resultado
        print('Você rolou um D10 e obteve:', resultado)


if dado == 'd12':
    for i in range(1,quantidade+1):
        resultado = random.randint(1,12)
        sum = sum+resultado
        print('Você rolou um D12 e obteve:', resultado)


if dado == 'd20':
    for i in range(1,quantidade+1):
        resultado = random.randint(1,20)
        sum = sum+resultado
        print('Você rolou um D20 e obteve:', resultado)

if dado == 'd100':
    for i in range(1,quantidade+1):
        resultado = random.randint(1,100)
        sum = sum+resultado
        print('Você rolou um D100 e obteve:', resultado)
                
print('\n'"Total:", sum)






# , end = ', '