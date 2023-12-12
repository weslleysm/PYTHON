#  faca um codigo que leia um nome de usuario e a sua senha e nao aceite a senha ingual ao nome de usuario
#  mostrando uma mensagem de erro e pedindo as informações novamente 

for i in range(1, 6):
    nome = input('informe seu nome de usuario:')
    senha = input('Informe sua senha:')
    if nome == senha:
        print(f'Erro! tentativa {i} de 5')
        
    else:
        break

