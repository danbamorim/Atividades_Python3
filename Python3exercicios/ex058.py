from time import sleep

primeiro = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))
fazer = 0
soma = 0
maior = 0
multiplicação = 0
while fazer != 5:
    print(''' 
       [1] soma
       [2] multiplicar 
       [3] maior
       [4] novos números
       [5] sair do programa''')
    sleep(0.5)
    fazer = int(input('>>>>> O que desejar fazer? '))
    if fazer == 1:
        soma = primeiro + segundo
        print('O resultado de {} + {} é {}'.format(primeiro,segundo,soma))
        sleep(0.7)
    elif fazer == 2:
        multiplicação = primeiro * segundo
        print('O resultado de {} vezes {} é {}'.format(primeiro,segundo,multiplicação))
        sleep(0.7)
    elif fazer == 3:
        if primeiro > segundo:
           maior = primeiro
        else:
           maior = segundo
        print('O número maior é {}'.format(maior))
        sleep(0.5)
    elif fazer == 4:
        print('Novos números')
        primeiro = int(input('Digite o primeiro número: '))
        segundo = int(input('Digite o segundo número: '))
        sleep(0.5)
    elif fazer == 5:
        print('Já vai? até logo')
        sleep(0.9)
        print('Finalizando...')
        sleep(0.9)
        print('A gente se vê por ai')
        sleep(0.9)