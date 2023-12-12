# faça um codigo que peca uma nota, entre 0 a 10, mostre uma mensagem caso a nota seja invalida e continue pedindo ate que
# o usuario informe uma nota valida.

while True:
    nota = float(input('Informe uma nota entre 0 a 10:'))
    if nota > 0 and nota < 10:
        print('Nota valida')
        break
    else:
        print('Nota invalida')