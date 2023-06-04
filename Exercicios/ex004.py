a = input('Digite algo: ')
print(type(a))

print('')

print(('{} | é número? {}'.format(a, a.isnumeric())))

print(('{} | é alfabético? {}'.format(a, a.isalpha())))

print(('{} | é alfanumérico? {}'.format(a, a.isalnum())))

print(('{} | está em maiúsculas? {}'.format(a, a.isupper())))

print(('{} | está em minusculas? {}'.format(a, a.islower())))

print(('{} | está capitalizada? {}'.format(a, a.istitle())))
