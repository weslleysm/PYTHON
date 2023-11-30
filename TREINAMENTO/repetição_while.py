# Supondo que a população de um pais A sejaa de 80000 habitantes com uma taxa anual de crescimento de 3%,
# Faça um programa que calcule e escreva o numero de anos necessarios para que a população do pais A chegue a 120000 habitantes
habitantes_atual = 80000
porcentagem_anual = (3 * habitantes_atual) / 100
anos = 0
valor_final = habitantes_atual
while True:
    crescimeto = porcentagem_anual
    valor_final = valor_final + crescimeto
    anos += 1
    if valor_final >= 120000:
        print(f'o crescimento anual e de {porcentagem_anual} e levara {anos} anos para atinir 120000 habitantes')
        break