# faça um programa que peça um numero inteiro e determine se ele é ou não um numero primo
# um numero primo é aquele que é divisivel somente por ele mesmo e por 1.
# 
numero = int(input('informe um numero interiro:'))
contador = 0
for i in range (1, numero+1):
    if numero % i == 0:
        print(f'foi divisivel por {i}')
        contador += 1
if contador == 2:
    print(f'o numero {numero} é primo')
else:
    print(f'o numero {numero} não é primo')