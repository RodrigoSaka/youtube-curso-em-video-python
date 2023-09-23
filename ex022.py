name = '    Paulo de Souza Marques    '.strip()

print('Analisando seu nome...')
print('Seu nome em maiusculas é {}'.format(name.upper()))
print('Seu nome em minusculas é {}'.format(name.lower()))
print('Seu nome tem ao todo {} letras'.format(len(name) - name.count(' ')))
# print('Seu primeiro nome tem {} letras'.format(name.find(' ')))
nameSplit = name.split()

print('Seu primeiro nome é {} e ele tem {} letras'.format(
    nameSplit[0], len(nameSplit[0])))
