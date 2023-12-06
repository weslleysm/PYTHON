# colocando uma dicionario dentro de uma lista

brasil = []
estado1 = {'uf':'ceara', 'sigla':'CE',}
estado2 = {'uf':'são paulo', 'sigla':'SP',}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)  # aqui nos mostra uma LISTA com DICIONARIOS dentro



print(50*'*')
print(brasil[0]) # vai mostrar o indice 0 da lista que é o dicionario estado1
print(brasil[0]['uf']) # usando a chave à frete do indice, nós trás um valor daquela chave que esta dentro do dicionario
print(50*'*') 
print(brasil[1]) # vai mostrar o indice 0 da lista que é o dicionario estado2
print(brasil[1]['uf']) # usando a chave à frete do indice, nós trás um valor daquela chave que esta dentro do dicionario 