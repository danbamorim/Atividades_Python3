def controle(largura,comprimento):
    total = largura * comprimento
    print(f'a area do terreno em largura {largura} e o  comprimento {comprimento} é de {total}')



print('=' * 30)
print('Controle de Terrenos')


l = float(input('Informe a largura:  '))
c = float(input('Informe o comprimento:  '))
controle(l,c)