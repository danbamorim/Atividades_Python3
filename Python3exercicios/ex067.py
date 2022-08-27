tot18 = 0
totM = 0
totF = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
      sexo = str(input('Sexo: ')).upper().strip()[0]
    if idade > 18:
      tot18 += 1
    if sexo == 'M':
       totM += 1
    if sexo == 'F' and idade < 20:
        totF += 1
    continuar = ' '
    while continuar not in 'SN':
          continuar = str(input('Quer continuar? S/N ')).upper().strip()[0]
    if continuar == 'N':
          break
print('Acabbbou')
print(f'Foram {tot18} maiores de 18 anos')
print(f'Foram {totM} homem cadastrado')
print(f'Foram {totF} mulheres menores de 20')
