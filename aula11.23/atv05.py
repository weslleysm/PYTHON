# faça um programa que peça um nome e imprima quantas vogais tem nesse nome 

contador = 0
nome = (input("informe um nome:"))
for i in nome:
    if i in 'aeiou':
        contador += 1

print(f'no nome {nome} tem {contador} vogais')
