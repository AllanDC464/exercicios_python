num = int(input('Digite um número: '))
n = num
numin = num

while n != 1:
    n = n - 1
    num = num * n
print('O fatorial de {} é {}'.format(numin, num))

# ↓ ↓ ↓ Resolução com for ↓ ↓ ↓

"""num = int(input('Digite um número: '))
n = num
numin = num

for c in range(1, num):
    n -= 1
    num = num * n
print('O fatorial de {} é {}'.format(numin, num))"""
