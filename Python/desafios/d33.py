a = int(input('Digite o primeiro numero'))
b = int(input(('Digite o segundo numero')))
c = int(input('Digite o terceiro número'))

menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

print('O menor valor é {}'.format(menor))

maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print('O maior valor é {}'.format(maior))
#if a<b and a<c:
#    menor = a
#if b<a and b<c:
#    menor = b
#if c<a and c<b:
#    menor = c
