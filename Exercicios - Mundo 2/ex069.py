contid = cadhom = contmu = 0
while True:
    print('▬' * 25)
    print('CADASTRE UMA PESSOA'.center(25))
    print('▬' * 25)
    idade = int(input('idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F] ')).strip().upper()[0]
    if sexo in 'M':
        cadhom += 1
    print('▬' * 25)
    if idade > 18:
        contid += 1
    if sexo in 'F' and idade < 20:
        contmu += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('======== FIM DO PROGRAMA ========')
print(f'foram cadastradas {contid} pessoas com mais de 18 anos')
print(f'Foram cadastrados {cadhom} homens')
print(f'Foram cadastradas {contmu} mulheres com menos de 20 anos')
