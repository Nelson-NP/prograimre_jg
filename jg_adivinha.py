
from random import randint 

pc = randint(0, 5)
num = int(input('Por favor, digite um número (entre 0 e 5)? '))

if num == pc:
    print('Certo, parabéns!')
else:
    print('Errado!')