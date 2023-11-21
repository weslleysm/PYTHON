#  faca um codigo que leia um nome de usuario e a sua senha e nao aceite a senha ugual ao nome de usuario
#  mostrando uma mensagem de erro e pedindo as informações novamente 

for w in range(1, 6):
    usuario = input('informe seu nome:')
    password = input('informe uma senha:')
    if usuario == password:
        print(f'Erro! Tentativa {w} de 5')
        if w == 5:
            print('Tente novamente depois.')
    else:
        break