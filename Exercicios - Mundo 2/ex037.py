num = int(input('Digite um número: '))
escolha = int(input('Escolha a base de conversão \n[1] Binário \n[2] Octal \n[3] Hexadecimal \nEscolha:'))

if escolha == 1:
    print('O número {} em binário fica {}'.format(num, format(num, 'b')))
elif escolha == 2:
    print('O número {} em octal fica {}'.format(num, format(num, 'o')))
elif escolha == 3:
    print('O número {} em hexadecimal fica {}'.format(num, format(num, 'x')))
else:
    print('Opção indisponivel! \nTente outra vez!')
