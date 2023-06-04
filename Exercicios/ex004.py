a = input('Digite algo: ')
print(type(a))

print(('{} | é numero? {}'.format(a, a.isnumeric())))

print(('{} | é palavra? {}'.format(a, a.isalpha())))

print(('{} | é letra ou numero? {}').format(a, a.isalnum()))
