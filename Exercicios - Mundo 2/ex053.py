frase = str(input('Digite uma frase: '))
frasem = frase.strip().lower().replace(' ', '')
inve = ''.join(reversed(frasem))
if frasem == inve:
    print('A frase \033[4;32m{}\033[m é um palindromo.'.format(frase))
else:
    print('A frase \033[4;31m{}\033[m não é um palindromo.'.format(frase))
