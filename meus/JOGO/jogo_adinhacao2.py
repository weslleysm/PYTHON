import random # A FUNÇÃO random SERVE PARA GERAR UM NUMERO ALEATORIO
def jogo2():
    print(40*"*")
    print("Bem vindo ao jogo de Adivinhação!")
    print(40*"*")
    numero_secreto = random.randrange(1,101) # A FUNÇÃO random.randragem(inicio, fim) SERVE PARA GERAR UM NUMERO ALEATORIO
    total_de_tentativas = 0
    pontos = 100

    print('Qual nivel de dificuldade?', numero_secreto)
    print('(1) Facil (2) Medio (3) Dificil')
    nivel = int(input('Defina o nivel: '))
    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5





    for rodada in range (1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número de 1 a 100: ")
        print("Você digitou " , chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Voce deve digite um numero de 1 a 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Parabéns! Você acertou e fez {} pontos".format(pontos))
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

            if(maior):
                print("O seu chute foi maior do que o número secreto!")
                if rodada == total_de_tentativas:
                    print('O numero secreto era {} voce fez {}'.format(numero_secreto, pontos))
            elif(menor):
                print("O seu chute foi menor do que o número secreto!")
                if rodada == total_de_tentativas:
                    print('O numero secreto era {}, voce fez {}'.format(numero_secreto, pontos))
        


    print("Fim do jogo")

if (__name__ == '__main__'):
    jogo2()