num = int(input('Deseja visualizar a tabuada de qual número: '))
numtab = int(input('Até qual número deseja que vá sua tabuada: '))
for c in range(1, numtab+1):
    print('{} x {:2} = {}'.format(num, c, num * c))
