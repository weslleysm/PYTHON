"""
Questão 08

• Escreva um programa que atenda as requisições abaixo e imprma todos os resultados:

01. peça três frutas para o usuario e calcule o total da compra dele
02. informe qual fruta tem o menor valor
03. faça uma promoção e diminua o preco de duas frutas para metade CONCLUID
04. insira duas novas frutas e seus preços                          CONCLUID0

"""


frutas = ["abacaxi", "uva", "maçã", "abacate", "tangerina"]
precos = [3.50, 4.99, 6.49, 9.10, 4.99]
dic_frutas = {}
for i, j in enumerate(frutas):
    dic_frutas.update({frutas:precos[i]})
print(dic_frutas)

print(frutas)
print(precos)
precos[0] = 1.75                            #03
precos[1] = 2.49
print(precos)


frutas.append("morango")
precos.append(6.0)
frutas.append('goiaba')
precos.append(5.0)
print(frutas)                              #04
print(precos)