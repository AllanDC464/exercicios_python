"""num = str(input('Digite um número de 0 a 9999: ')).zfill(4)
print('\nO número digitado foi: {}'.format(num))
print('Sua unidade é: {}'.format(num[3]))
print('Sua dezena é: {}'.format(num[2]))
print('Sua centena é: {}'.format(num[1]))
print('seu milhar é: {}'.format(num[0]))"""

num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))
