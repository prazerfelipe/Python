r1 = int(input('Digite o comprimento da primeira reta'))
r2 = int(input('Digite o comprimento da segunda reta'))
r3 = int(input('Digite o comprimento da terceira  reta'))
f= (r2 - r3)<r1<r2<(r2+r3)
if f :
    print('é possivel')
else:
    print('Não é possivel')