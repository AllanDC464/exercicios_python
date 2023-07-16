tabelaDoBrasileirão = ('', 'Botafogo', 'Flamengo', 'Grêmio', 'Fluminense', 'Palmeiras', 'Bragantino', 'Fortaleza', 'São Paulo', 'Cruzeiro', 'Internacional', 'Athletico-PR', 'Atlético-MG', 'Santos', 'Cuiabá', 'Corinthians', 'Bahia', 'Goiás', 'Coritiba', 'Vasco da Gama', 'América-MG')

print('\033[32;4mTabela completa do brasileirão\033[m')
for c in range(1, len(tabelaDoBrasileirão)):
    print(f'{c:>2} {tabelaDoBrasileirão[c]}')
print('')

print('\033[32;4mCinco Primeiros colocados na tabela do brasileirão\033[m')
for c in range(1, 6):
    print(f'{c} {tabelaDoBrasileirão[c]}')
print('')

print('\033[32;4mQuatro últimos colocados na tabela do brasileirão\033[m')
for c in range(-4, 0):
    print(f'{tabelaDoBrasileirão.index(tabelaDoBrasileirão[c])} {tabelaDoBrasileirão[c]}')
print('')

print('\033[32;4mTimes em ordem alfabetica\033[m')
tab = sorted(tabelaDoBrasileirão)
for c in range(1, 21):
    print(f'{tabelaDoBrasileirão.index(tab[c]):>2} {tab[c]}')
print('')

print('\033[32;4mEm que posição esta o Athletico-PR\033[m')
print(f'O Athletico-PR esta na  {tabelaDoBrasileirão.index("Athletico-PR")}ª posição')
