from datetime import date
nasc = int(input('Informe o ano de nascimento: '))
ano = date.today().year
idade = ano - nasc
if idade < 18:
    print('Seu alistamento será em {} ano(s)!'.format(18 - idade))
elif idade == 18:
    print('Você esta na idade de se alistar!')
else:
    print('Você passou {} ano(s) do tempo de se alistar!'.format(idade - 18))
