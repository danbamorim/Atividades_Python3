tuplas = ('zero' , 'um' , 'dois', 'três', 'quatro','cinco','seis','sete','oito','nove','dez','onze', 'doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
     numero = int(input('Escolhe um número de 0 a 20:  '))
     if 0 <= numero <= 20:
         break
     print('Tenta novamente pamonha')
print(f'Voce digitou {tuplas[numero]}')