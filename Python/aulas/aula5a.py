Condição simples

nome = str(input('Qual e seu nome ?')).strip()
if nome == 'Felipe':
    print('Que nome lindo que você tem')
else:
  print('Que nome tão normal')
print("Bom dia, {}!".format(nome))

#Condição composta
n1 = float(input("Digite sua primeira nota"))
n2 = float(input("Digite sua segunda nota "))
m= (n1+n2)/2

print('Sua média é {:.1f}'.format(m))

if m>= 6.0:
    if m>=8.0:
        print("Deitasse feio")
    print('Sua média esta aprovada! PARABÉNS')
else:
    if m<=5:
        print("Venha conversa com nos porque vamos te ajudar ")
    print('Puxa vida, acontece mas não desista que você consegue,sabemos disso!')

