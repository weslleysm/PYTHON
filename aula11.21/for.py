#'for' trabalha com iteraveis! ele tem que possuir uma variavel de controle
#metodos do for: inter() - tranforma um objeto em iteravel
#                next() - função par imprimir os iteraveis de uma 'lista'


# enumerate() - é um iterador de indices e valores
lista_nomes = ['joão', 'pedro', 'mateus', 'judas', 'tiago']

lista_enumerada = enumerate(lista_nomes)

print(lista_nomes)
print(list(lista_enumerada))

for item in lista_enumerada:
    print(item)

for indice_lista, item_lista in enumerate (lista_nomes):
    print(f'{item_lista} é o {indice_lista} da lista')

