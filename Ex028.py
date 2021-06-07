from random import randint
compu = randint(0, 5)
print('vou pensar em um número entre 0 e 5. tente adivinhar..')
jogador = int(input('Em que número eu pensei? '))
if jogador == compu:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {compu} e não no {jogador}!')
    