primeiro = float(input('Primeiro segmento: '))
segundo = float(input('Segundo segmento: '))
terceiro = float(input('Terceiro segmento: '))

if primeiro <segundo + terceiro and segundo < primeiro + terceiro and terceiro < segundo + primeiro:
    print('Os segmentos dá para formar um tringulo')
else:
    print('Os segmentos não dá para formar um triangulo')