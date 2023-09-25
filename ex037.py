num = int(input('Digite um número inteiro: '))

print('Escolha uma das bases para conversão:')
print('[ 1 ] Converter para BINÁRIO')
print('[ 2 ] Converter para OCTAL')
print('[ 3 ] Converter para HEXADECIMAL')

opcao = int(input('Sua opção: '))

if opcao == 1:
    resultado = bin(num)[2:]
    print('{} convertido para BINÁRIO é igual a {}'.format(num, resultado))
elif opcao == 2:
    resultado = oct(num)[2:]
    print('{} convertido para OCTAL é igual a {}'.format(num, resultado))
elif opcao == 3:
    resultado = hex(num)[2:]
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, resultado))
else:
    print('Opção inválida. Tente novamente!')
