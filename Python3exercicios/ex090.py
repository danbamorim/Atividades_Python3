from datetime import datetime

dado = dict()
dado['nome'] = str(input('nome: '))
ano = int(input('data de nascimento: '))
dado['idade'] = datetime.now().year - ano
dado['carteira'] = int(input('carteira de trabalho [0] nao tem :  '))

if dado['carteira'] != 0:
    dado['ano de contratacao'] = int(input('ano que foi contratada: '))
    dado['salario'] = int(input('salario:  '))
    dado['aposentadoria'] = dado['idade'] + (dado['ano de contratacao'] + 35) - datetime.now().year

for k, v in dado.items():
    print(f'{k} tem o valor {v} ')

