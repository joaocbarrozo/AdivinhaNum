print("""Vamos jogar um jogo, eu vou escolher um número entre 0 e 10 e sua missão é adivinha-lo.
Você tem três chances.""")
import random
x = random.randrange(0, 10)
#print(x)
vidas = 3
while vidas > 0:
    y = int(input('Qual número eu estou pensando? '))
    if y == x:
        print('Parabéns você acertou !!!')
        quit()
    elif y < x:
        print('O número que estou pensando é maior do que',y)
    else :
        print('O número que estou pensando é menor do que',y)
    vidas -= 1
    if vidas > 1:
        print('Vamos lá, você ainda tem', vidas,'chances')
    elif vidas == 1:
        print('Pense bem, essa é sua ultima chance!')
    else:
        print('Oh não você perdeu, suas chances acabaram.')
        print('O número que eu estava pensando era',x)
