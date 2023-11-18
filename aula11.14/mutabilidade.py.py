# Alguns cuidados com dados mutaveis 
# Mutaveis - são dados que podem ter seu valor alterado na memoria do dispositivo
# Imutaveis - são dados que so podem ser copiados da memoria do dispositivo

lista = ['joão', 'paulo']
lista[1] = 'jose'
print(lista)

#strings são totalmente mutaveis 
nome = 'paulo' 
# nome = 'joão'
# nome[2] = 'a'
novo_nome = nome
nome = 'joão'
print(nome)
print(novo_nome)

#listas são mutaveis e imutaveis 
lista_a = ['joão', 'paulo']
lista_b = lista_a.copy()
lista_c = lista_b
lista_a[1] = 'jose'
print(lista_a)
print(lista_b)
print(lista_c)
