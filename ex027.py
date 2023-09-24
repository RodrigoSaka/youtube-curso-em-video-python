nome = input('Dgite seu nome completo: ').strip()
nomeArray = nome.split()

print('Seu primeiro nome é {}'.format(nomeArray[0]))
print('Seu último nome é {}'.format(nomeArray[len(nomeArray)-1]))
