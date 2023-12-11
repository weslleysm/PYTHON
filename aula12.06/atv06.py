# faz um quiz utilizando um dicionario com as seguintes chaves: pergunta, opçoes e respostas. Faça a validação da 
# opção escolida com a resposta e imprima.

dic_quiz = {
            'perguntas':'Quem faz pão? ',
            'opções':['padeiro', 'pedreiro', 'medico'],
            'resposta':'padeiro',
}

for i in range (1, 4):
    resposta = input(dic_quiz['perguntas'])
    for i, opcao in enumerate(dic_quiz['opções']):
        print(f'Escolha uma das opções: {opcao}')
    resposta = input(dic_quiz['perguntas'])
    if resposta == dic_quiz['resposta']:
        print('Parabens, voce acertou')
        break
    elif resposta == dic_quiz['opções'][1] or resposta == dic_quiz['opções'][2]:
        print(f'Resposta errada! Tentativa {i} de 3.')
        if i == 3:
            print('Tente novamente depois')
    else:
        print(f'Resposta não existe! Tentativa {i} de 3.')
        if i == 3:
            print('Tente novamente depois')