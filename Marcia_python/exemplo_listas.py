print('====lista====')
n = [65, 66,61 ,62]
print('lista: ',n)
print('quantidade de elementos da lista: ', len(n))
print('Menor elemento da lista: ',min(n))
print('Maior elemento da lista: ', max(n))
n.append(5)
print('Acrescentando elemento no final da lista: ', n)
del n[2]
print('Deletando elemento da segunda posição da lista: ', n)
n.reverse()
print('Invertendo a ordem dos elementos da lista: ', n)
n.sort()
print('Ordenando os elementos da lista: ', n)
print('Verifica se existe o elemento 2 na lista: ', n, 2 in n)
print('Verifica se existe o elemento 5 na lista: ', n, 5 in n)
print('Somando os elementos da lista: ', n, sum(n))
n.extend(['João','Maria'])
print('Adicionando uma lista com strings: ',n)

        
    
