from random import randint
from time import sleep

compurador = randint(0, 5)

print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)

jogador = int(input('Em que número eu pensei? '))

print('PROCESSANDO...')
sleep(2)

if jogador == compurador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(compurador, jogador))
