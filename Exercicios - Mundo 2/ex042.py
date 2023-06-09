r1 = float(input('1º segmento: '))
r2 = float(input('2º segmento: '))
r3 = float(input('3º segmento: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Os segmentos acima formam um triangulo ', end='')
    if r1 == r2 and r2 == r3:
        print('equilátero!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('isóceles!')
    else:
        print('escaleno!')
else:
    print('Os segmentos acima não podem formar um triangulo!')
