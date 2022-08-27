import random
primeiro= str(input('Primeiro aluno : '))
segundo = str(input('Segundo aluno : '))
terceiro= str(input('Terceiro aluno : '))
quarto = str(input('Quarto aluno : '))
alunos = [primeiro, segundo, terceiro, quarto]

random.shuffle(alunos)

print('A sequencia é : ')
print(alunos)
