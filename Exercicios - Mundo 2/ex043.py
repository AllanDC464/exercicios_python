peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura**2)
if imc > 40:
    print('Obesidade mórbida')
elif imc > 30:
    print('Obesidade')
elif imc > 25:
    print('Sobrepeso')
elif imc > 18.5:
    print('Peso ideal')
elif imc < 18.5:
    print('Abaixo do peso')

print('Seu IMC é de {:.1f}'.format(imc))