somaidade = 0
medialidade = 0
idadehomem = 0
nomedovelho = ''
quantas_mulheres = 0
for p in range(1,5):
    print('{} Pessoa'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('M / F : ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
     idadehomem = idade
     nomedovelho = nome
    if sexo in 'Mm' and idade > idadehomem:
     idadehomem = idade
     nomedovelho = nome
    if sexo in 'Ff' and idade < 20 :
     quantas_mulheres +=1
medialidade = somaidade / 4
print('a media de todas as idades é {} '.format(medialidade))
print('O homem mais velho tem {} anos e se chama {}'.format(idadehomem,nomedovelho))
print('Tem {} mulheres menores de 20'.format(quantas_mulheres))



