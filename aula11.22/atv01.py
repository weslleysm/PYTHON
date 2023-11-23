

contador_par = 0
contador_impar = 0
for i in range (1, 11):
    numero1 = int(input(f'informe o {i}º numero: '))
    if numero1 % 2 == 0:
        contador_par += 1
    else:
        contador_impar += 1

print(f'a quantidade de numeros pares é: {contador_par}')
print(f'a quantidade de numeros impares é: {contador_impar}')