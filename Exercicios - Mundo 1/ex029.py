velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
    print('\033[1;31mSua velocidade: {}km\033[m \n\033[1;32mVelocidade Permitida: 80km\033[m \n\033[1;31mMulta sobre a velocidade excedida: R${:.2f}!\033[m'.format(velocidade, (velocidade - 80) * 7))
print('\033[1;36mTudo em ordem!\033[m')
print('\033[1;36mTenha um otimo dia! Dirija com segurança!\033[m')