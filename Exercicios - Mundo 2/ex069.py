contid = cadhom = contmu = 0
resp = 'Ss'
while resp in 'Ss':
    print('▬' * 25)
    print('CADASTRE UMA PESSOA'.center(25))
    print('▬' * 25)
    idade = int(input('idade: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo [M/F] '))
        if sexo in 'Mm':
            cadhom += 1
    print('▬' * 25)
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
    while resp not in 'Ss':
        resp = str(input('Quer continuar? [S/N] '))
    if idade > 18:
        contid += 1
    elif sexo in 'Ff' and idade < 20:
        contmu += 1
print('======== FIM DO PROGRAMA ========')
print(f'foram cadastradas {contid} pessoas com mais de 18 anos')
print(f'Foram cadastrados {cadhom} homems')
print(f'Foram cadastradas {contmu} mulheres com menos de 20 anos')
