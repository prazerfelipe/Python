n = input ('Digite algo:')
print('Qual o tipo: {}'.format(type(n)) )
print('É um numero ? {}'.format(n.isalnum()))
print('É numerico?{}'.format(n.isnumeric()))
print('É alfanumerico?{}'.format(n.isalpha()))
print(n.isascii())
print(n.isdigit())
print(n.isdecimal())
print(n.isidentifier())