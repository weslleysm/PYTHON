# Fatiamento de strings
# Obs: toda string por padrão é uma lista que não saiu do armario
# Ordem de tratamento 
# 0123456.......
# -654321.......
# [i:f:p] = i - INICIO, i - FIM, p - PARSE

nome = "Rodrigo Jose dos Santos Amaral Neto Junior"
print(nome[17:23]) # inicio
print(nome[-6:]) # fim
print(nome[0::2]) # parse -> pares
print(nome[1::2]) # parse -> impares


print("="*20)
lista_nome = ("p","a","u","l","o")
print(nome [3])
print(nome [-2])
print(lista_nome [3])
print(lista_nome [-2])

