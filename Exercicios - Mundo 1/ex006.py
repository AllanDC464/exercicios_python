from math import sqrt

n = int(input('Digite um número: '))
raiz = sqrt(n)
print('O dobro de {} é: {}\nO triplo de {} é: {}\nA raiz quadrada de {} é: {:.1f}'.format(n, n*2, n, n*3, n, raiz))

# tambem é possivel descobrir a raiz quadrada desse forma: n**(1/2)
