primeiro = int(input('Calcular seu fatorial: '))
razao = int(input('Calcular seu fatorial: '))
termo = primeiro
cont = 1

while cont <=10:
     print('{}  -> '.format(termo),end= '')
     termo += razao
     cont += 1
print('Fim')