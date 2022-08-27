import random
primeiro= str(input('Primeiro aluno : '))
segundo = str(input('Segundo aluno : '))
terceiro= str(input('Terceiro aluno : '))
quarto = str(input('Quarto aluno : '))
aluno = (primeiro, segundo, terceiro, quarto)
escolhido = random.choice(aluno)

print('O aluno escolhido é:{} '.format(escolhido))
