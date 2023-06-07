from math import sin, cos, tan, radians
ang = int(input('Digite um ângulo: '))
print('Ângulo = {}° \nSeno = {:.2f} \nCosseno = {:.2f} \nTangente = {:.2f}'.format(ang, sin(radians(ang)), cos(radians(ang)), tan(radians(ang))))
