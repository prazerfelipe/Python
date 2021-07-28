import math
cad = float(input( 'Digite o valor do cateto Adjacente'))
cop = float(input('Digite o valor do cateto Oposto'))
h = math.hypot(cop, cad)
print(' A hipotenusa vai medir {:.2f}'.format(h))