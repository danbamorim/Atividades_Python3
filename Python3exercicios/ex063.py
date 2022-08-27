resp = 'Ss'
media = 0
maior = 0
menor = 0
quant = 0
soma = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1
    if quant == 1:
      maior = num
      menor = num
    else:
        if num > maior:
          maior = num
        if num < menor:
          menor = num
    resp = str(input('Quer continuar? S ou N? ')).upper().strip()[0]
media = soma/ quant
print('O maior  é {} e o menor é {}'.format(maior,menor))
print('Vocẽ escreveu {} numeros e a média foi de {} '.format(quant,media))