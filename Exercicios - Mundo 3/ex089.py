dados = []
nome = []
notas = []
while True:

    nome.append(str(input('Nome: ')))
    for c in range(1, 3):
        notas.append(float(input(f'Nota {c}: ')))
    nome.append(notas[:])
    dados.append(nome[:])
    nome.clear()
    notas.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continura? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
        
print()
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>12}')
print('▬' * 28)

i = 0
for c in dados:
    print(f'{dados.index(dados[i]):<4}{c[0]:<10}{(c[1][0] + c[1][1]) / 2:>10.1f}')
    i += 1
while True:
    mostrarNota = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if mostrarNota == 999:
        print('ENCERRANDO...')
        break
    else:
        print(f'Notas de {dados[mostrarNota][0]} são {dados[mostrarNota][1]}')
