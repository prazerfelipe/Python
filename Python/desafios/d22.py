nome = str(input("Qual é o seu nome completo?")).strip()



print('Analisando seu nome...')
print('Seu nome em letra maiuscula é {}'.format(nome.upper()))
print('Seu nome em letra minuscula é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro  nome é {} e ele tem {} letras '.format(separa[0], len(separa[0]) ))