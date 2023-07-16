palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for c in range(0, len(palavras)):
    print(' ')
    print(f'Na palavra {palavras[c]} temos', end=' ')
    for i in list(palavras[c]):
        if i in 'AEIOU':
            print(i, end=' ')
            