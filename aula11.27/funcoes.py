# funçoes são blocos de codigos que são executados somente quando são chamados
# parametro: def
# OBS: as funçoes devem ter prioridade no codigo

def media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

nota01 = int(input('Informe a primeira nota:'))
nota02 = int(input('Informe a segunda nota:'))
nota03 = int(input('Informe a terceira nota:'))
print(media(nota01, nota02, nota03 ))

nota04 = int(input('Informe a quarta nota:'))
nota05 = int(input('Informe a quinta nota:'))
nota06 = int(input('Informe a sexta nota:'))
print(media(nota04, nota05, nota06))


def calcula_hora_extras(valorBruto, quantidadedeHoras):
    calcula_hora_extras = (valorBruto / quantidadedeHoras) * 0.5
    return calcula_hora_extras

quantidade_horas = float(input('Informe a quantidade de horas trabalhadas:'))
valor_bruto = float(input('Informe a taxa do colaborador:'))

print(calcula_hora_extras(quantidade_horas, valor_bruto))