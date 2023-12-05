"""
Questão 08

• Escreva uma função que calcule o tempo de viagem de uma pessoa lembre de imprmir todos os resultados:

01. peça a distancia e a velocidade media
02. a formula é: distância / velocidade média(hora)
03. não esqueça de limitar a respota em apenas duas casas decimais 

"""
# o comando "round" limita a quabtidade de casas decimais que voce deseja

distancia = int(input('Informe a distancia:'))
velocidade_m = int(input('Informe a velocidade media:'))
tempo_viagem = round (distancia / velocidade_m, 2)
print(tempo_viagem)