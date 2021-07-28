num = int(input('Escolha um numero de 0 a 9999'))
u = num// 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando seu número...')
print('Unidade:{}'.format(u))
print('Dezena:{}'.format(d))
print('Centenas:{}'.format(c))
print('Milhar:{}'.format(m))
