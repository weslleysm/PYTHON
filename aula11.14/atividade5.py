# 5-faca um codigo que crie uma lista com 20 numeros inteiros e armazene os numeros pares na lista pares e os
# numeros impares na lista impar, printe as duas listas 
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lista_pares = lista_numeros[1::2]
lista_impares = lista_numeros[0::2]
print('numeros pares:', lista_pares)
print('numeros impares:', lista_impares)