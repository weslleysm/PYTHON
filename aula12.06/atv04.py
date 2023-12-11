# 4 crie um cadastro de clientes recebendo nome, idade, data de aniversario e endereço 
# completo (rua,numero da residencia e bairro) adicione todas as informaçoes em um dicionario. imprima ao final
cadastro_clientes = {}
cadastro_clientes['nome'] = str(input('Informe seu nome:'))
cadastro_clientes['idade'] = int(input('Informe sua idade:'))
cadastro_clientes['data de aniversario'] = float(input('Informe sua data de anoversario'))
cadastro_clientes['rua'] = str(input('Informe sua rua:'))
cadastro_clientes['numero da residencia'] = int(input('Informe seu numero da residencia:'))
cadastro_clientes['bairro'] = str(input('Informe o bairro que voce reside:'))
print(cadastro_clientes)
