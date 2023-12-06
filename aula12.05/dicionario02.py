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
print(len(pessoa))
print(50 * '*')
print(pessoa.keys())
print(50 * '*')
print(pessoa.values())

print(50 * '*')
for chave in pessoa:
    print(chave)

print(50 * '*')
v = pessoa.values()
for chave in v:
    print(chave)

for chave in pessoa.values():
    print(chave)

print(50 * '*')
for chave, valor in pessoa.items():
    print(chave, valor)

print(50 * '*')
print(pessoa['nome'], pessoa['sobrenome'])

print(50 * '*')
d1 = {'valor1':'100',
      'valor2':'200',
      'valor3':'300', }
d2 = d1.copy()
print(d1)
d2['valor2'] = 2000
print(d1)
print(d2)
print(d2.get('valor2'))
d3 = d1.pop('valor3')
print(d1)
dic = {'valor5':'5',
         'valor6':'6'}
d1.update(dic)
print(d1)
#print(d1.has_key('valor5'))

print(50 * '*')
# EXEMPLO:
pessoas = {'nome':'weslley', 'sexo':'masculino', 'idade':'23'}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')