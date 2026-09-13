
from random import randint 

tent = 3
certo = errada = 0

while (tent > 0):
    pc = randint(0, 5)
    num = int(input('Por favor, digite um número (entre 0 e 5)? '))

    if num == pc:
        print('Certo, parabéns!')
    else:
        print('Errado!')
    tent -= 1

print('Pontuação final:')
print(f'Certo = {certo}\nErrada = {errada}')