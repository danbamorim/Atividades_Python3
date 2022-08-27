num = list()
par = list()
impar = list()

while True:
   num.append(int(input('Digite um valor: ')))
   continua = str(input('Quer continuar? S/N '))
   if continua in 'Nn':
         break
for i, v in enumerate(num):
    if v % 2 == 0:
       par.append(v)
    else:
        impar.append(v)
print(f'Voce escolheu os numero {num}')
print(f'Os numeros pares sao {par}')
print(f'Os numeros impares sao {impar}')