dicionario = dict()
dicionario['nome'] = str(input('nome:   '))
dicionario['nota'] = float(input(f'Media de {dicionario["nome"]}:   '))

if dicionario['nota'] >= 7:
    dicionario['situacao'] = 'Aprovado'
elif 5 <= dicionario['nota'] < 7 :
    dicionario['situacao'] = 'RecuperaçÂo'
else:
    dicionario['situacao'] = 'Nem mamando o diretor passa'


for k, v in dicionario.items():
    print(f'{k} é igual {v} ')


