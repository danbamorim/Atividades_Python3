galera = list()
pessoa = dict()
soma = media = 0
while True:
   pessoa.clear()
   pessoa['nome'] = str(input('Qual o nome? '))
   while True:
       pessoa['sexo'] = str(input('Qual o sexo? M/F ')).upper()[0]
       if pessoa['sexo'] in 'MF':
          break
       print('Erro! digite novamente : apenas M/F')
   pessoa['idade'] = int(input('Qual a idade? '))
   soma += pessoa['idade']
   galera.append(pessoa.copy())
   while True:
       contin = str(input('Quer continuar? S/N  ')).upper()[0]
       if contin in 'SN':
          break
       print('Erro! digite novamente : apenas S/N')
   if contin == 'N':
          break
print('='* 30)
print(galera)
print(f' A) Ao todo temos {len(galera)} pessoas')
media = soma/len(galera)
print(f' B) A média de idades é {media}')

print(f' C) As mulheres cadastradas foram:', end=' ')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}')

print(f' D) As pessoas acima da media sao : ' , end = ' ')
for p in galera:
    if p['idade'] >= media:
        print('       ')
        for k , v in p.items():
            print(f'{k} = {v}' , end=' ')
        print()







