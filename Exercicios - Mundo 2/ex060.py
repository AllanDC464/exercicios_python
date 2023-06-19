num = int(input('Digite um número para calcular o fatorial: '))
n = num
numin = num
print('Calculando {}! = '.format(num),end='')
while n != 1:
    print(n, end=' x ')
    n -= 1
    num *= n
print('1 = {}'.format(num))



# ↓ ↓ ↓ Resolução com for ↓ ↓ ↓

"""num = int(input('Digite um número para calcular o fatorial: '))
n = num
numin = num
print('Calculando {}! = '.format(num),end='')
for c in range(1, num):
    print(n, end=' x ')
    n -= 1
    num *= n
print('1 = {}'.format(num))"""



# ↓ ↓ ↓ Resolução com método ↓ ↓ ↓

"""from math import factorial
n = int(input('Digite um número para calcular o fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))"""
