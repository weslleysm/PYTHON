# keys - keys() retorna uma lista com todas as chaves do dicionário.
# values - values() retorna uma lista com todos os valores do dicionário.
# items - items() retorna uma lista com todos os pares chave/conteúdo do dicionário.
# has_key - has_key(chave)
# dic.has_key(chave) é o mesmo que chave in dic.

# fromkeys - Retorna um novo dicionário cujas chaves são os elementos de lista e cujos valores são todos iguais a valor. Se valor não for especificado, o default é None.
# copy - Retorna um outro dicionário com os mesmos pares chave/conteúdo.
# clear - Remove todos os elementos do dicionário.
# get - Obtém o conteúdo de chave. Não causa erro caso a chave não exista: retorna valor. Se o valor não for especificado, chaves inexistentes retornam None.
# update - Atualiza um dicionário com os elementos de outro Os itens em dic são adicionados um a um ao dicionário original. É possível usar a mesma sintaxe da função dict para especificar dic.
# popitem - Retorna e remove um par chave/valor aleatório do dicionário. Pode ser usado para repetir sobre todos os elementos do dicionário.
# pop - Obtém o valor correspondente a chave e remove o par chave/valor do dicionário.
# possuem CHAVE(KEYS) e VALOR(VALUES) 
# parametro: {} ou dict()
# 
pessoa = { # chave  valor
            'nome':'paulo',
            'sobrenome':'junior',
            'nome1':'paulo1',
            'sobrenome1':'junior1',}
print(len(pessoa)) # len pode ser usado nos dict para fazer a contagem de quantos valores tem dentro do dict
print(50 * '*')
print(pessoa.keys())# keys nos mostra todas as chaves que tem dentro do dict
print(50 * '*')
print(pessoa.values())#values nos mostra todos os valores que tem dentro do dict

print(50 * '*')
for chave in pessoa:
    print(chave)    # exemplo de impressão de chaves com estrutura de repetição for

print(50 * '*')
v = pessoa.values()
for chave in v:     # exemplo 1 de impressão de valores com estrutura de repetição for
    print(chave)

print(50*'*')
for chave in pessoa.values():
    print(chave)    # exemplo 2 de impressão de valores com estrutura de repetição for

print(50 * '*')
for chave, valor in pessoa.items():
    print(chave, valor) # exemplo de impressão de CHAVES e VALORES com repetição for

print(50 * '*')
print(pessoa['nome'], pessoa['sobrenome']) #impressão de mais de um valores especificos 

print(50 * '*')
d1 = {'valor1':'100',
      'valor2':'200',  # um novo dicionario
      'valor3':'300', }
d2 = d1.copy() # copy() para fazer uma copia de um dicionario
print(d1)
d2['valor2'] = 2000 # mudando o valor da chave do d2, que é a copia do d1
print(d1)           # d1 nao vai sofrer alteração, pois o d2 tem indentidade propia apos ser uma copia
print(d2)           # alteração apenas no d2
print(50*'*')
print(d2.get('valor2')) #get serve para imprimir apenas um valor especifico
print(d2['valor2'])     #porem voce pode fazer sem o get, usando apenas a senha dentro de []cochetes
print(50*'*')
d3 = d1.pop('valor3')  # pop pode ser usado para deletar um item informando a sua senha
del d1['valor1']       # del pode ser usado para deletar um item informando a sua senha
print(d1)
print(50*'*')
dic = {'valor5':'5',
         'valor6':'6'}
d1.update(dic)   # update tras um dict para junção/atualização de outro  
print(d1)

print(50 * '*')
# EXEMPLO:
pessoas = {'nome':'weslley', 'sexo':'masculino', 'idade':'23'}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') # aqui temos a interpolação de strigs com dict