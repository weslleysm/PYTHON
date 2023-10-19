# 7 Faça um programa que peça 3 numeros inteiros.
#   Calcule e imprima :
#  -O produto "multiplicação" do dobro do primeiro com metade do segundo somado com o terceiro. 
#  -A soma do triplo do primeiro com o terceiro e multiplicado pelo segundo.

n1 = input("Digite o primeiro numero:" )
n2 = input("Digite um segundo numero:" )
n3 = input("digite um terceiro numero:" )

resultado01 = 2 * int(n1) + int(n2) / 2

resultado02 = 3 * int(n1) + int(n3) * int(n2)

print("Primeiro calculo:", resultado01)
print("Segundo calculo:", resultado02)