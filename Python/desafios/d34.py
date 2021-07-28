s = float(input('Qual é o se sálario?'))

if s<=1250:
    sn =s*1.15
    print('Seu Sálario antes do aumento era {} agora ele é {:.2f} ele recebeu um aumento de 15%'.format(s,sn))
else:
    sn = s* 1.1
    print('Seu Sálario antes do aumento era {} agora ele é {:.2f} ele recebeu um aumento de 10%'.format(s,sn))