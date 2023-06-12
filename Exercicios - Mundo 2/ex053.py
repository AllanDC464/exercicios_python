frase = str(input('Digite uma frase: ')).lower()
frasem = frase.strip().replace(' ', '')
inve = ''.join(reversed(frasem))
if frasem == inve:
    print('A frase \033[4;32m{}\033[m é um palindromo, e ao contrario fica \033[4;32m{}\033[m.'.format(frase, inve))
else:
    print('A frase \033[4;31m{}\033[m não é um palindromo, e ao contrario fica \033[4;31m{}\033[m.'.format(frase, inve))
