viagem = float(input('Qual a distancia da sua viagem?'))

pas2 = viagem * 0.45
if viagem<= 200  :
    pas1 = viagem * 0.50
    print('O preço da passagem sera R${:.2f}'.format(pas1))
else:

   print('O preço da sua passagem é R${:.2f}'.format(pas2))
