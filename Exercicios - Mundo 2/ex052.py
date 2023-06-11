num = int(input('Digite um número: '))
for c in range(2, num):
    if num % 2 == 0:
        print('Não é primo')
        break
    else:
        print('É primo')
        break
if num == 0 or num == 1:
    print('Não é primo')
elif num == 2:
    print('É primo')
