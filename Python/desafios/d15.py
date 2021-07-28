dia = int(input('Qantos dias ficou alugado?'))
km = float(input('Quantos KM rodados?'))

d= dia*60
rd= km*0.15
r= d+rd

print('o total a pagar é R${:.2f}'.format(r))