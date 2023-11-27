def escolha():

    import jogo_adinhacao2
    import foca

    print (40 * '*')
    print("Escolha o Jogo!")
    print(40 * '*')

    print('(1) Adivinhação (2) Foca')

    jogo = int(input('Qual jogo?'))

    if jogo == 1:
        print('jogo de adivinhação')
        jogo_adinhacao2.jogo2()
    elif jogo == 2:
        print('jogo de foca')
        foca.jogo1()

if (__name__ == '__main__'):
    escolha()