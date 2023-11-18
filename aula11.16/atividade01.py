# imprima na tela os pares dentro de uma lista chamada pares_ok
# remova da lista os multiplos de 4

meus_numeros = []
meus_numeros = [0, 1, 2, 3, 4, 5, 6,7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
pares_ok = meus_numeros [2:21:2]
print(pares_ok, type(pares_ok))
del meus_numeros [0:21:4]
print(meus_numeros, type(meus_numeros))
