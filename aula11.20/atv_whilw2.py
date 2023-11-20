#  faca um codigo que leia um nome de usuario e a sua senha e nao aceite a senha ugual ao nome de usuario
#  mostrando uma mensagem de erro e pedindo as informações novamente 

while True:
    nome = input('informe seu nome ')
    senha = input('informe seu nome ')
    if nome == senha:
        print(f'Erro, nome de usuario {nome} igual a senha {senha}')
    else:
        break

