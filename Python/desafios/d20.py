from random import shuffle
pes1 = input ('Primeiro Aluno')
pes2 = input ('Segundo Aluno')
pes3 = input('terceito Aluno')
pes4 = input( 'Quarto Aluno')

lista = [pes1,pes2,pes3,pes4]
shuffle(lista)
print("a ordem de apresentação será")
print(lista)