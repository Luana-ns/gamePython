from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('\nSuas opções: \n[ 0 ] PEDRA \n[ 1 ] PAPEL \n[ 2 ] TESOURA')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
print('KEN')
print('PO!!!')
print('-=' * 18)
print(f'Computador jogou {itens[computador]}.')
print(f'Jogador jogou {itens[jogador]}.')
print('-=' * 18)

