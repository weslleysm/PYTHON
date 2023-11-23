# Supondo que a população de um pais A sejaa de 80000 habitantes com uma taxa anual de crescimento de 3%,
# Faça um programa que calcule e escreva o numero de anos necessarios para que a população do pais A chegue a 120000 habitantes

inicial = 80000
aumento_anual = (3 * inicial) / 100
contador = 0
valorfinal = inicial

while True:
    aumento = aumento_anual
    valorfinal += aumento
    contador += 1

    if valorfinal >= 120000:
        print(f'Há cada ano cresce {aumento_anual} habitantes, levando {contador} anos para atingir um valor de {valorfinal} habitantes')
        break