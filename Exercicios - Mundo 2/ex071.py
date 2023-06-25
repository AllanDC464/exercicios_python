valor = qtc50 = qtc20 = qtc10 = qtc1 = 0

print('=' * 36)
print('BANCO ALL'.center(36))
print('=' * 36)

saque = int(input('Digite o valor a ser sacado R$'))
while valor < saque:
    if saque >= 50:
        saque -= 50
        qtc50 += 1

    elif saque >= 20:
        saque -= 20
        qtc20 += 1

    elif saque >= 10:
        saque -= 10
        qtc10 += 1

    elif saque >= 1:
        saque -= 1
        qtc1 += 1
    
if qtc50 != 0:
    print(f'Total de {qtc50} cédulas de R$50,00')
    
if qtc20 != 0:
    print(f'Total de {qtc20} cédulas de R$20,00')

if qtc10 != 0:
    print(f'Total de {qtc10} cédulas de R$10,00')

if qtc1 != 0:
    print(f'Total de {qtc1} cédulas de R$1,00')

print('=' * 36)
print('Volte sempre ao BANCO ALL! Tenha um bom dia!')
