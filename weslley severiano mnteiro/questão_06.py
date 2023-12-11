"""
Questão 06

• Escreva um programa que atenda as requisições abaixo e imprma todos os resultados:

01. crie uma nova lista só com os numeros pares. CONCLUIDA
02. crie uma nova lista só com os numeros impares.CONCLUIDA
03. crie uma nova litsa só com os multiplos de 2.
04. some todos os itens da "lista" 
05. informe quais valores se repetem

"""

lista = [10,11,20,22,30,33,40,11,50,55,60,66,70,22,80,88,90,99]

lista_par = []
for i in lista:
    if i % 2 == 0:
        lista_par.append(i)
print(lista_par)

lista_impar = []
for i in lista:
    if i % 2 != 0:
        lista_impar.append(i)
print(lista_impar)

lista_mult = []
for i in lista:
    if i // 2 * 2 == i:
        lista_mult.append(i)
print(lista_mult)

soma = 0
for i in lista:
    soma = soma + i
print(soma)

lista_repete = []
for i in lista:
    if lista.count(i) > 1 and i not in lista_repete:
        lista_repete.append(i)
print(lista_repete)