def aumentar(preço = 0 ,taxa = 0):
   aute = preço + (preço * taxa / 100)
   return aute


def dobro(preço = 0 ):
    dobe = preço * 2
    return dobe


def metade(preço = 0 ):
    met = preço / 2
    return met

def moeda(preço = 0 , moeda ='R$'):
    return f'{moeda}{preço}'.replace('.',',')

