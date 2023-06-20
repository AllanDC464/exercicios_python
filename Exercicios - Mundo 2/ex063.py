n1 = 0
n2 = 1

print('▬' * 30)
print(' Frequência de Fibonacci'.center(30))
print('▬' * 30)

qtdTermos = int(input('Quantos termos você quer mostrar? '))

c = 0
while c != qtdTermos:
    if c < qtdTermos:
        print(n1, end=' → ')
        c = c + 1
        n1 = n1 + n2
    if c < qtdTermos:
        print(n2, end=' → ')
        c  = c + 1
        n2 = n2 + n1
print('FIM')
