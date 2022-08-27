list = []
for l in range(0,5):
    digite = int(input('Digite um valor: '))
    if l == 0:
        list.append(digite)
    elif l > len(list)-1:
        list.append(digite)
        print('Adicionado ao final da lista ...')
    else:
        pos = 0
        while pos < len(list):
            if l <= list[pos]:
                list.insert(pos,l)
                print('Adicionado ao inicio da lista')
                break
            pos += 1
print(f'vc adicionou os numeros {list}')