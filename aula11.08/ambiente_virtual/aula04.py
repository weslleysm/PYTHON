# outra forma de INTERPOLAR (imprimir)
nome = "Weslley"
salrio = 4499.90

print(nome, "ganha um salario de R$", salrio)
print(f'O salrio de {nome} é R$ {salrio}') 

#Formula FORMAT de imprimir
# s = string
# d/i = int
# f = float 
# x e X = hexadecimais

print('O salario de %s é R$ %f' % (nome, salrio))

#formula (.format)
print('O {} ganha um salario de R$ {}' .format(nome, salrio))