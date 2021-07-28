frase = str(input("Digite uma frase")).strip().upper()

print('Sua Frase é: {}'.format( frase))
print('tem: {} "A"'.format(frase.count('A')))
print(' A primeira letra A apareceu na posição:{}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição: {}'.format(frase.rfind("A")+1))