# faça um codigo que peca uma nota, entre 0 a 10, mostre uma mensagem caso a nota seja invalida e continue pedindo ate que
# o usuario informe uma nota valida.

nota0 = 0
while nota0 < 9:
    nota = float(input('informe uma nota:'))
    if nota > 0 and nota < 10:
        print ('nota invalida')
    else:
        break

nota0 = nota0 + 1