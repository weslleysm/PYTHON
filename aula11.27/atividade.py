# Faça um programa, com uma uma função que necessite de um argumento. 
# A função retorna o valor de caractere 'P', se seu argumento for positivo, e 'N', se seu argumento for zero ou negativo.

def media(nota01, nota02, nota03):
    media = (nota01 + nota02 + nota03) / 3
    return media

nome01 = int(input('Informe o 1º n:'))
nome02 = int(input('Informe o 2º n:'))
nome03 = int(input('Informe o 3º n:'))
print(media(nome01, nome02, nome03 ))
