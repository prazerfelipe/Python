velocidade =int(input('Digite sua velocidade atual'))

if velocidade > 80:
   print('MULTADO! Você execedeu o limite permitido de 80 Km/h')
   multa = (velocidade -80)*7
   print('Você deve pagar uma multa de R${:.2f}'.format(multa))

print(' tenha um bom dia, dirija com segurança')