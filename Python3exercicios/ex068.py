totcompra = 0
tot1000 = 0
menor = 0
cont = 0
nomedomenor = ' '
while True:
    produto = str(input('Nome do produto: ')).strip()
    preço = float(input('Preço: R$'))
    cont+=1
    totcompra += preço
    if preço > 1000:
      tot1000 += 1
    if cont == 1:
        menor = preço
        nomedomenor = produto
    else:
        if preço < menor:
            menor = preço
            nomedomenor = produto
    resp = ' '
    while resp not in 'SN':
       resp = str(input('Quer continuar? S/N ')).strip().upper()[0]
    if resp == 'N':
        break
print('Acabou')
print(f'O total é {totcompra}')
print(f'Tem {tot1000} produtos custando mais de 1000R$')
print(f'O menor preço é do Produto {nomedomenor} que custa R${menor} ')