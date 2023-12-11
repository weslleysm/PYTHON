
# metodo CRUD - created, readed, update e deleted

dic = {'nome':'paulo',} # created
dic2 = dict(idade = 23) # created

dic['nome'] # readed
reading = dic2.get('idade')# readed

dic.update(sobrenome='junior') # update > inserindo dados
dic.update({'idade':23})# inserindo dados no dicionario
tupla = ('peso', 72.12),
dic.update(tupla)              #UPDATE
lista = ['data', '13/04/1996'], # sempre que voce quiser adicionar apenas uma tupla ou uma lista dentro do dicionario
dic.update(lista)               # voce deve usar a , virgula no final, se for mais de uma não é necessario


print(dic)
print(dic2)

dic.clear() # Deleted
print(f'dados do dicionario:{dic}')
