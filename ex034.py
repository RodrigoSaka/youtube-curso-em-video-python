salario = float(input('Qual é o seu salario? '))

if salario <= 1250:
    aumento = salario * 0.15
else:
    aumento = salario * 0.10

novo_salario = salario + aumento

print('Quem ganhava R${:.2f}, passa a receber R${:.2f}'.format(
    salario, novo_salario))
