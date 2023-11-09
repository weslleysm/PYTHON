entrada = input('[E] para entrar e [S] para passar: ')
senha_digitada = input('Digite a senha: ')
senha = "12345678"
if (entrada == 'E' or entrada == 'e'):
    if (senha == senha_digitada):
        print('Sucesso, voce entrou!')
    else:
        print('Voce não entrou, senha incorreta!')
elif (entrada == 'S' or entrada == 's'):
    if (senha == senha_digitada):
        print('Voce escolheu PASSAR')
    else:
        print('Voce não passou, senha incorreta')
else:
    print('Voce não escolheu uma opção valida!')
