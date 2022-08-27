soma = 0
cont = 0
while True:
    num = int(input('Digite um número(aperta 999 que acaba)  '))
    if num == 999:
         break
    soma += num
    cont += 1
print(f'A soma dos {cont} valores foi {soma}')