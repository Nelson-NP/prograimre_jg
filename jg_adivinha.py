
from random import randint 

tent = 5
certo = errada = 0

while (tent > 0):
    pc = randint(0, 5)
    num = int(input('Por favor, digite um número (entre 0 e 5)? '))

    if num == pc:
        print('Certo, parabéns!')
        certo += 1
    else:
        print('Errado!')
        errada += 1
    tent = tent - 1

print('Pontuação final:')
print(f'Certo = {certo}\nErrada = {errada}')