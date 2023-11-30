# 1 crie uma lista com cinco nome de alunos do curso de alunos do back-end.
#   a. imprima a lista
#   b. adicione um sexto nome da lista 
#   c. remova o terceiro indice da lista 
#   d. remova um objeto especifico da lista 
#   e. imprima a lista 
#   f. adicione um novo nome na lista

lista = []
lista = ['joao', 'weslley', 'jose', 'anderson', 'alice']
print(lista)
lista.append('paulo')
del lista[2]
lista.remove('joao')
print(lista)
lista.append('mateus')
print(lista)