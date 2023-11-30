#  faca um codigo que leia um nome de usuario e a sua senha e nao aceite a senha ingual ao nome de usuario
#  mostrando uma mensagem de erro e pedindo as informações novamente 

tentativa = 1
while tentativa <= 5:
    usuario = input('Informe seu nome:')
    senha = input('Informe sua senha:')
    if usuario == senha:
        print(f'Erro! tentativa {tentativa} de 5')
        if tentativa == 5:
            print('Tente novamente depois.')
    else:
        print('Usuario e Senha criado com sucesso.')
        break
    tentativa += 1

# essa mesma estrutura pode ser feita com for 