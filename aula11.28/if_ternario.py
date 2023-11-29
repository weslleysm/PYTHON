# condição ternaria acontecce em formato de linha.

salario = float(input('Informe o valor do seu salario:'))

if salario >= 2500.00:
    print('IR sera cobrado')
else:
    print('IR não sera cobrado')

variavel_controle = 'IR sera cobrado' if salario >= 2500.00 else 'IR não sera cobrado'
print(variavel_controle)

vr_controle = 'Ok 1' if False else 'Ok 2' if False else 'Fim'
print(vr_controle)

if False:
    print('Ok 1')
elif False:
    print('Ok 2')
else:
    print('Fim')