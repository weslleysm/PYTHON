# 1 crie uma lista de alunos com nome e nota final de cada aluno e coloque em um diciionario, depois imprima.


lista = [['weslley', 10], ['joao', 11]]
dicionario = {}
dicionario.update(lista)
print(dicionario)


print(50*'*')
# 2 ainda sobre a questão 1. inserir mais 4 alunos e notas no seu dicionario
dicionario.update({'raimundo':4})
dicionario.update({'manoel':8})
dicionario.update({'jose':7})
dicionario.update({'livia':9})
print(dicionario)