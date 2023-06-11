ma = 0
me = 0
for c in range(1, 6):
    peso = float(input('Digite o peso: '.format(c)))
    if c == 1:
        ma = peso
        me = peso
    else:
        if peso > ma:
            ma = peso
        if peso < me:
            me = peso
print('O maior peso lido foi de {}Kg'.format(ma))
print('O menor peso lido foi de {}Kg'.format(me))
