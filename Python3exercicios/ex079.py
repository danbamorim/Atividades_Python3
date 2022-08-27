list = []
while True:
   list.append(int(input('Digite um valor: ')))
   continua = str(input('Quer continuar? S/N '))
   if continua in 'Nn':
         break
print('=' * 30)
print(f'Voce adicionou {len(list)} valores')
list.sort(reverse= True)
print(f'Vocẽ adicionou os numeros {list}')
if 5 in list:
    print('O numero 5 aparece na listagem')
else:
    print('O numero 5 nao aparece')