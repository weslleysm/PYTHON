nome = "weslley"
altura = 1.80
peso = 75
imc = peso / (altura * altura)
print(nome, "tem", altura, "de altura")
print( "pesa", peso, )
print("e seu IMC é", imc )
# a resposta dessa questão deve ser:
# fulano tem ALTURA  de altura, pesa PESA quilos e seu IMC é: 
# valor
print(f'{nome} tem {altura: .2f} de altura, pesa {peso} quilos e seu imc é:')
print(f'{imc:.2f}')