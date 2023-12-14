# CONVERSÃO DE DINHEIRO
# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ele pode comprar.
# considere US$1,00 = R$4,95
#           EUR1,00 = 5,35


real = float(input('Quanto voce tem na sua carteira?R$'))
dolar = real / 4.95
euro = real / 5.35
print(f'Com R${real:.2f} voce pode comprar US${dolar:.2f}')
print(f'com R${real:.2f} voce pode comprar EUR{euro:.2f}')
