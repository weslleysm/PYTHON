"""
Questão 08

• Escreva um programa que atenda as requisições abaixo e imprma todos os resultados:

01. peça três frutas para o usupario e calcule o total da compra dele
02. informe o qual fruta tem o menor valor
03. faça uma promoção e diminua o preco de duas frutas paara metade CONCLUID
04. insira duas novas frutas e seus preços                          CONCLUID0

"""

frutas = ["abacaxi", "uva", "maçã", "abacate", "tangerina"]
precos = [3.50, 4.99, 6.49, 9.10, 4.99]
precos[0] = 4.00                            #03
precos[1] = 5.00
print(precos)


frutas.append("morango")
precos.append(6.0)
print(frutas)                              #04
print(precos)