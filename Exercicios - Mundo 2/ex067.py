while True:
    tab = int(input('Quer ver a tabuada de qual valor? '))
    if tab < 0:
        break
    print('▬' * 40)
    for c in range(1, 11):
        print(f'{tab} x {c:2} = {tab * c}')
    print('▬' * 40)
print('▬' * 40)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
