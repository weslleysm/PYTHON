# com meus_numeros = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# imprima na tela os multiplos de 3 em uma lista chamada multiplos_ok
# remova de meus_numeros os multiplos de 5   

meus_numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

multiplos_ok = []
multiplos_ok = meus_numeros[0:21:3]
print(multiplos_ok, type(multiplos_ok))

del meus_numeros [0:21:5]
print(meus_numeros, type(meus_numeros))
