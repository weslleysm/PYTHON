#  faca um codigo que leia um nome de usuario e a sua senha e nao aceite a senha ugual ao nome de usuario
#  mostrando uma mensagem de erro e pedindo as informações novamente 

i = 1
while i < 4: 
    nome = input('informe seu nome ')
    senha = input('informe seu nome ')
    if nome == senha:
        print(f'Erro, tentativa {i} de 3.')
        i = i + 1
    else:
        break