print('\033[33m-=-\033[m' * 10)
print('\033[1;32m   Analisador de triângulos   \033[m')
print('\033[33m-=-\033[m' * 10)
r1 = float(input('\033[32m1º segmento:\033[m '))
r2 = float(input('\033[32m2º segmento:\033[m '))
r3 = float(input('\033[32m3º segmento:\033[m '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('\033[34mOs segmentos acima \033[1;4mPODEM FORMAR\033[m \033[34mtriangulo\033[m')
else:
    print('\033[31mOs segmentos acima não \033[1;4mPODEM FORMAR\033[m \033[31mtriangulo\033[m')
