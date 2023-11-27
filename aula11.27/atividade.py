# Faça um programa, com uma uma função que necessite de um argumento. 
# A função retorna o valor de caractere 'P', se seu argumento for positivo, e 'N', se seu argumento for zero ou negativo.

def media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

nome01 = int(input('Informe o 1º nome:'))
nome02 = int(input('Informe o 2º nome:'))
nome03 = int(input('Informe o 3º nome:'))
print(media(nome01, nome02, nome03 ))
