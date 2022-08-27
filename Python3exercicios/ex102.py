def leiaInt(msg):
    nada = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
           valor= int(n)
           nada = True
        else:
            print("Erro tio")
        if nada:
           break
    return valor




n = leiaInt('DIgite um numero: ')
print(f'Vc acabou de digitar o numero {n}')