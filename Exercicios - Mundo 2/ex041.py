from datetime import date
ano_nasc = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
if idade < 0:
    print('\033[1;30;41mIdade invalida!\033[m')
elif idade > 25:
    print('O atleta tem {} anos.'.format(idade))
    print('O atleta esta na categoria \033[34mMASTER\033[m!')
elif idade > 19:
    print('O atleta tem {} anos.'.format(idade))
    print('O atleta esta na categoria \033[34mSÊNIOR\033[m!')
elif idade > 14:
    print('O atleta tem {} anos.'.format(idade))
    print('O atleta esta na categoria \033[34mJUNIOR\033[m!')
elif idade > 9:
    print('O atleta tem {} anos.'.format(idade))
    print('O atleta esta na categoria \033[34mINFANTIL\033[m!')
else:
    print('O atleta tem {} anos.'.format(idade))
    print('O atleta esta na categoria \033[34mMIRIM\033[m!')
