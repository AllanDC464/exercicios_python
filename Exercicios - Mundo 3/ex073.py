tabelaDoBrasileirão = ('', 'Botafogo', 'Flamengo', 'Grêmio', 'Fluminense', 'Palmeiras', 'Bragantino', 'Fortaleza', 'São Paulo', 'Cruzeiro', 'Internacional', 'Athletico-PR', 'Atlético-MG', 'Santos', 'Cuiabá', 'Corinthians', 'Bahia', 'Goiás', 'Coritiba', 'Vasco da Gama', 'América-MG')

print('Cinco Primeiros colocados na tabela do brasileirão')
for c in range(1, 6):
    print(f'{c}', tabelaDoBrasileirão[c])
print('')

print('Quatro últimos colocados na tabela do brasileirão')
for c in range(-4, 0):
    print(f'{tabelaDoBrasileirão.index(tabelaDoBrasileirão[c])}', tabelaDoBrasileirão[c])
print('')

print('Times em ordem alfabetica')
tab = sorted(tabelaDoBrasileirão)
for c in range(1, 21):
    print(f'{tabelaDoBrasileirão.index(tab[c]):>2}', tab[c])
print('')

print('Em que posição esta o Athletico-PR')
print('O Athletico-PR enta na posição ', tabelaDoBrasileirão.index('Athletico-PR'))
