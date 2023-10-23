# 2. Receba a altura(h) de uma pessoa, crie um código que calcule seu peso ideal, utilizando as fórmulas abaixo:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
    
    #peso ideal para homens
altura_h = float(input('Digite a altura do homem:'))
peso_h   = (72.7 * altura_h) - 58
print('Peso ideal do homem:', peso_h)
    
    # peso ideal para mulheres 
altura_m = float(input('Digite a altura da mulher:'))
peso_m   = (62.1 * altura_m) - 44.7
print('Peso ideal da mulher:', peso_m)