tab = 0
while True:
    num = 0
    tab = int(input('Quer ver a tabuada de qual valor? '))
    if tab < 0:
        break
    print('▬' * 40)
    while num != 10:
        num += 1
        print(f'{tab} x {num:2} = {tab * num}')
    print('▬' * 40)
print('▬' * 40)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
