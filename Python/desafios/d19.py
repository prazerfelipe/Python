import random
pes1 = input ('Primeiro nome')
pes2 = input ('Segundo nome')
pes3 = input('terceito nome')
pes4 = input( 'Quarto nome')

lista = [pes1, pes2, pes3, pes4]
escolhido = random.choice(lista)

print('O aluno escolhido foi {}'.format(escolhido))