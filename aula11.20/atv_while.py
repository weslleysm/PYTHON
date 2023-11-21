# faça um codigo que peca uma nota, entre 0 a 10, mostre uma mensagem caso a nota seja invalida e continue pedindo ate que
# o usuario informe uma nota valida.

rodada = 1
while rodada < 6:
    nota = float(input('informe uma nota:'))
    if nota > 0 and nota <= 10:
        print (f'Nota invalida, tentativa {rodada} de 5')
        rodada = rodada + 1
    else:
        print('Valida')
        break

