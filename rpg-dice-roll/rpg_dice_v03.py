# Título: Rolador de Dados de RPG
# Autor: @robsonfvilela
# Versão: 3.0
# Data: 2022-08-23
# Changelog: 

# Versão 2.0:
# - Agora pode escolher quantos dados rolar. Adicionado d100.

# Versão 2.2:
# Agora a quantidade de dados é digitada junto com o nome do dado. (o limite para a quantidade é 9)

# Versão 3.0 (2022-08-23)
# - O código foi reescrito e simplificado.
# - Usando "split", não é preciso reptir o código para cada tipo de dado.
# - Agora é possível rolar entre 1 e 99 dados.
# - É possível rolar dados que não existem, como D3, por exemplo.

import random
import time

print('='*60)
print(f'''
Este é um rolador de dados simples.

Para utilizá-lo:
1. Digite o nome do dado que deseja jogar (Ex.: d4, d6, d8 etc.);
2. Caso deseje rolar mais de um dado, digite o número antes (Ex.: 2d6).

OBS.: O limite de dados a serem rolados é 99.
''')
print('='*60)
print('------------')
dado = input('Dado: ').upper()

#print(' ')

digito1 = dado[0:1]
digito2 = dado[1:2]
digito3 = dado[2:3]

print('------------')

time.sleep(0.5)
sum = 0

# Se for rolado apenas 1 dado (sem digitar a quantidade antes do nome do dado):
if digito1 == 'D':
    numero_do_dado = int(dado[1:])

    for i in range(1,2):
        resultado = random.randint(1,numero_do_dado) # o random vai de 1 até o número do dado
        sum = sum+resultado
        print(f'Você rolou um D{numero_do_dado} e obteve:', resultado)

# Se forem rolados entre 1 e 9 dados (digitando a quantidade antes do nome do dado):
if digito2 == 'D':
    quantidade_dado = int(dado[0:1]) # Quntos dados serão rolados
    numero_do_dado = int(dado[2:]) # Número do dado que será rolado

    for i in range(1,quantidade_dado+1):
        resultado = random.randint(1,numero_do_dado) # o random vai de 1 até o número do dado
        sum = sum+resultado
        print(f'Você rolou um D{numero_do_dado} e obteve:', resultado)

# Se forem rolados entre 10 e 99 dados (digitando a quantidade antes do nome do dado):
if digito3 == 'D':
    quantidade_dado = int(dado[0:2]) # Quntos dados serão rolados
    numero_do_dado = int(dado[3:]) # Número do dado que será rolado

    for i in range(1,quantidade_dado+1):
        resultado = random.randint(1,numero_do_dado) # o random vai de 1 até o número do dado
        sum = sum+resultado
        print(f'Você rolou um D{numero_do_dado} e obteve:', resultado)

if digito1 != 'D' and digito2 != 'D' and digito3 != 'D':
    print('Você não digitou um dado válido. \nOu tentou rolar mais de 99 dados!')

print('\n'"TOTAL:", sum)
