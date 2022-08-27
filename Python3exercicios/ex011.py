largura= float(input('Quantas larguras?'))
altura= float(input('Quanto de altura?'))

area = largura * altura

print('Para pintar a parede, tu tem a dimensao de {:.2f}x{:.2f} e e sua área é de {}m2'.format(largura,altura,area))

tinta = area / 2

print('E para tinta tu vai ter {}'.format(tinta))