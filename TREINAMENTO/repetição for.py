# faça um programa que peça um nome e imprima quantas vogais tem nesse nome 
rodada = 0
nome = input('informe um nome')
for i in nome:
    if i in 'aeiou':
        rodada = rodada + 1
print(f'no nome {nome} contém {rodada} vogais e {len(nome)} digitos')