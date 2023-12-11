# 5 vamos criar um sistema de login e senha.
# crie um dicionario contendo os acessos dos colaboradores com nome de usuario e senha. 
# em seguida peça as informaçoes e valide o login do usuario.

dic_acessos = {'weslley':'12345', 'livia':'54321'}
usuario = input('Informe seu login:')
senha = input('informe sua senha:')
usuario_senha = {}
usuario_senha = {usuario:senha}

for chave in dic_acessos.keys():
    if chave == usuario:
         if dic_acessos[chave] == senha:
            print('Acesso liberado')
            break
         else:
            print(f'o usuario {usuario} digitou a senha incorreta')
            break
else:
    print('usuario não encontrado')