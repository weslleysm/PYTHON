# uma lista é representada pelos [] cochetes 
# OBS: todo metodo por obrigação ele retorna algum valor
# len - metodo que retorna a quantidade de itens de uma lista 
# append - metodo que insere itens no final da lista
# del - remove item especifico da lista 
# remove - remove um objeto especifico da lista
# pop - remove o ultimo objeto da lista
# insert - ele adiciona um objeto no inicio da lista 
# estend - junta duas listas 

# metodo LIST normal é representada pelo []
lista = ['front']
print(lista, type(lista))
print(len(lista))
lista = ['back']
print(lista, type(lista))
print(len(lista))

# 'append' é um metodo LIST, ele pega a penultima "variaveis.append" e coloca valores no fim da lista
lista.append('data')
print(lista, type(lista))
print(len(lista))
lista.append('front')
print(lista, type(lista))
print(len(lista))

#           0        1      2   3     4
# Reverse  -5       -4     -3   -2    -1 
lista = [ 'back', 'tarde', 21, True, 8.8 ]
print(f' a quantidade de alunos na turma é {lista [2]}')
lista[2] = 22
print(lista)
lista[1] = False
print(lista)
lista [1] = ['neyva', 'alice', 'lara', 'paula', 'geisa'] # matriz 
print(lista[1][2])

print(lista)
del lista[-2] # del remove pelo indice
print(lista)
print(lista)
del lista[-2]
print(lista)
print(lista)
del lista[-2]
print(lista)
lista.remove('back') # o .remove deleta pelo o valor
print(lista)


lista.append(26)
lista.append(27)
lista.append(100)
print(lista)
valor_do_pop = lista.pop()
print(lista)
print(f'foi removido da lista o cliente de id {valor_do_pop}') # o pop alem da 

lista.insert(0, 'amontada valley') # insert adiciona objeto no inicio, meio ou fim
print(lista)
lista.insert(2, 'professor')
print(lista)
