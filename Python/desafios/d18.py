import math

ang = float(input('Digite um ângulo qualquer'))
cos = math.cos(math.radians(ang))
sen = math.sin(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O ângulo {} tem cosseno {:.2f} , seno {:.2f} e tangente {:.2f}'.format(ang,cos,sen,tan))