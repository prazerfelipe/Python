import random
from time import sleep

print('Pensei em numero tente acertar, Uma dica é esse número esta entre 0 á 5 ')
num= int(input('Digite o número que você acha que é'))
n = int(random.randint(0,5))
print('PROCESSANDO...')
sleep(2)
if num == n :
    print('Caraca você realmente acertou! o número foi {}'.format(n))
else:
    print('Puxa vida não foi dessa vez tente mais,sei que uma hora vai,o número foi {}'.format(n))
