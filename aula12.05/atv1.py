# aqui usamos uma estrutura de repetição for, dentro adiconamos a SENHA e com um input adicionamos o VALOR
# logo em seguida com o 'append' inserimos o DICIONARIO dentro da LISTA, usando o "copy()" para fazer uma copia
# Formando assim um DICIONARIO dentro de uma LISTA

estado = {}
brasil = []
for i in range(1,3):
    estado['uf'] = str(input('nome do estado:'))
    estado['sigla'] = str(input('sigla do estado:'))
    brasil.append(estado.copy())
print(brasil)