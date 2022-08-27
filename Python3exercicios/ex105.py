def leiaInt(msg):
     while True:
           try:
               n = int(input(msg))
           except (TypeError, ValueError):
                 print('Digite um valor inteiro novamente: ')
                 continue
           else:
               return n


def leiafloat(msn):
     while True:
           try:
               f = int(input(msn))
           except (TypeError, ValueError):
                 print('Digite um valor real novamente: ')
                 continue
           else:
               return f


num = leiaInt(input('Digite um número inteiro válido?  '))
print (f'O resultado é {num}')
real = leiafloat(input('Digite um valor real: '))
print (f'O resultado é {num} e {real}')