# 3 faça um codigo que pede a marca e o modelo do carro do cliente insere ele em uma lista e depois tranforma em um 
# dicionario. imprima os dois resultados



marca = input('Informe a marca do carro:')
modelo = input('Informe o modelo do carro:')
lista_carros = []
lista_carros.append(marca)
lista_carros.append(modelo)

dic_carros = {}
dic_carros.update([lista_carros])
print(lista_carros)
print(dic_carros)

# Adicione um item no dicionario
print(50*'*')
dic_carros.update({'Fiat':'Uno'}) # melhor forma de adicionar um item no dicionario
print(dic_carros)

