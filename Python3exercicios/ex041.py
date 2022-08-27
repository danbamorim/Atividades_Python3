segmento1 = int(input('Primeiro segmento: '))
segmento2 = int(input('Segundo segmento: '))
segmento3 = int(input('Terceiro segmento: '))


if segmento1 == segmento2 == segmento3:
    print('Será formado por equilatero')
elif segmento1 == segmento2 or segmento2 == segmento3 or segmento3 == segmento1:
    print('Se chama Isóceles')
else:
    print('se chama escaleno')