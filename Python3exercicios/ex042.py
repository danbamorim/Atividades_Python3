peso = float(input('Qual seu peso: '))
altura = float(input('Qual sua altura: '))


IMC = peso / (altura * altura)

print('O seu IMC é de {:.2f}'.format(IMC))

if IMC < 18.5:
     print('Está Abaixo do peso')
elif IMC >= 18.5 and IMC < 25:
     print('Parabens! está no peso ideal')
elif IMC >= 25 and IMC  < 30:
     print('Sobrepeso')
elif  IMC >= 30 and IMC < 40:
     print('Cuidado gordox esta na fase da Obesidade')
elif IMC > 40:
     print('Gordo do carai')

